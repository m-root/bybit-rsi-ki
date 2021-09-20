from datetime import datetime
import pytz, time
from core import log
from engine import trading_logic
from core.utilities import Utilities
from payload.pl_tasks import telegram_message_relay


####################################
#              PAYLOAD             #
####################################

class Payload(object):

    def __init__(self, base_asset=None, cross_asset=None, chat_id=None, settings=None,  period=None, time_frame=None):
        self.settings = settings
        self.baseAsset = base_asset
        self.quoteAsset = cross_asset
        self.pair = self.baseAsset + self.quoteAsset
        self.chat_id = chat_id
        self.time_frame = time_frame
        self.rest_client = settings.rest_client
        self.trade_logic = trading_logic.TradingLogic(
            pair=self.pair,
            settings=settings,
            period = period,
            tFrame = time_frame
        )



        log.debug_info(self.pair)
        # log.debug_info(self.exchangeInfo)
        log.debug_info('Base Asset : {}'.format(self.baseAsset))
        log.debug_info('Quote Asset : {}'.format(self.quoteAsset))
        # log.debug_info('Get Ticker Price : {}'.format(auth.getTickerPrice()))
        # log.debug_info('Get Cross Asset Balance : {}'.format(auth.getCrossBalance()))
        # log.debug_info('Get Base Asset Balance : {}'.format(auth.getBaseAssetBalance()))
        # log.debug_info('Cross Asset Converted Balance : {}'.format(auth.getCrossAssetBalance()))
        # log.debug_info('Base Asset Converted Balance : {}'.format(auth.getBaseConvertBalance()))

    def buy_logic(self):

        if self.trade_logic.buyLogic():

            print('--------------01----------------')
            if self.settings.trade:
                auth = Utilities(self.settings.api_key,
                                 self.settings.secret_key,
                                 self.baseAsset,
                                 self.quoteAsset,
                                 )

                balance = auth.getMarginCrossAssetBalance()
                print(balance)
                print('--------------02----------------')
                if balance > self.settings.min_order_val:
                    price = auth.getTickerPrice()
                    minPricedp = self.exchangeInfo.minPricedp()
                    minQtydp = self.exchangeInfo.minQtydp()
                    price = round(price - 1 / 10 ** minPricedp, minPricedp)

                    if self.settings.marginEnabled:
                        balance = auth.getMarginCrossLoanBalance()
                        print('--------------2.1----------------')
                        print(balance)
                        quantity = auth.getCrossBalanceConv(balance=float(balance))
                        quantity = round(quantity - 1 / 10 ** minQtydp, minQtydp)

                    else:
                        quantity = auth.getCrossBalanceConv(balance=balance)
                        quantity = round(quantity - 1 / 10 ** minQtydp, minQtydp)

                    print('--------------03----------------')
                    log.debug_info(
                        'Buy Attempt : Pair : {}, Price : {}, Quantity : {}'.format(self.pair, price,
                                                                                    quantity))

                    log.debug_info('********** MARKER 5 *****************')
                    log.debug_warning(self.rest_client.TIME_IN_FORCE_GTC)
                    log.debug_info('********** MARKER 5 *****************')

                    try:
                        trade_details = self.settings.rest_client.create_margin_order(
                            symbol=self.pair,
                            side=self.rest_client.SIDE_BUY,
                            type=self.rest_client.ORDER_TYPE_LIMIT,
                            timeInForce=self.rest_client.TIME_IN_FORCE_GTC,
                            quantity=quantity,
                            price=str(price)
                        )
                        time.sleep(self.settings.sleep_time)
                        log.debug_info(auth.cancelMarginOrders(trade_details['orderId']))

                        try:
                            telegram_message_relay(
                                settings=self.settings,
                                telegram_message=trade_details
                            )
                            try:
                                log.debug_info('Trade ID is : {}'.format(trade_details))
                            except Exception as e:
                                log.debug_error('Catch Error : 01 : {}'.format(e))
                        except Exception as e:
                            log.debug_error('Catch Error : 02 : {}'.format(e))

                    except Exception as e:
                        log.debug_error('Catch Error : 03 : {}'.format(e))

                    log.debug_info('********** MARKER 6 *****************')

                    '''auth.getCrossMinBalance()'''

                    while auth.getCrossMinBalance() < quantity:
                        ticker_price = auth.getTickerPrice()
                        log.debug_info('Ticker Price : {}, Price : {} '.format(ticker_price, price))
                        if ticker_price != price:

                            price = auth.getTickerPrice()
                            minQtydp = self.exchangeInfo.minQtydp()
                            newq_tp = auth.getBaseAssetBalance()
                            newq_tp = round(newq_tp - 1 / 10 ** minQtydp, minQtydp)
                            newq_tp = quantity - newq_tp
                            log.debug_info(
                                'Sell Retrial Attempt : Pair : {}, Price : {}, Quantity : {}'.format(self.pair, price,
                                                                                                     newq_tp))

                            try:
                                trade_details = self.settings.rest_client.create_margin_order(
                                    symbol=self.pair,
                                    side=self.rest_client.SIDE_BUY,
                                    type=self.rest_client.ORDER_TYPE_LIMIT,
                                    timeInForce=self.rest_client.TIME_IN_FORCE_GTC,
                                    quantity=quantity,
                                    price=str(price)
                                )
                                time.sleep(self.settings.sleep_time)
                                log.debug_info(auth.cancelMarginOrders(trade_details['orderId']))
                                time.sleep(self.settings.sleep_time)

                                try:
                                    log.debug_info('Trade ID is : {}'.format(trade_details))
                                except Exception as e:
                                    log.debug_error('Catch Error : 04 : {}'.format(e))
                            except Exception as e:
                                log.debug_error('Catch Error : 05 : {}'.format(e))

                            if not auth.getMarginCrossAssetBalance() > self.settings.min_order_val:
                                break

                    telegram_message = 'BINANCE SIGNAL : BUY : {} Price : {}  Time {} Asia/Hong_Kong time ' \
                        .format(
                        self.pair, float(auth.getTickerPrice()),
                        str(datetime.now(pytz.timezone('Asia/Hong_Kong'))

                            )
                    )
                    log.debug_info('{}'.format(telegram_message))

                    try:
                        telegram_message_relay(
                            settings=self.settings,
                            telegram_message=telegram_message
                        )
                    except Exception as e:
                        log.debug_error('Catch Error : 06 : {}'.format(e))

            if self.trade_logic.buyLogic():
                log.debug_info('We are currently long on {}'.format(self.pair))

    ####################################
    #          SELL ENTRY LOGIC        #
    ####################################
    def sell_logic(self):

        if self.trade_logic.sellLogic():

            if self.settings.trade:
                auth = Utilities(self.settings.api_key,
                                 self.settings.secret_key,
                                 self.baseAsset,
                                 self.quoteAsset,

                                 )
                balance_conversion = auth.getBaseConvertBalance()
                log.debug_info('Base Asset Converted Balance : {}'.format(balance_conversion))
                log.debug_info('Logic Test : {}'.format(balance_conversion > self.settings.min_order_val))

                print(auth.getBaseConvertBalance())

                if auth.getMarginBaseConvertBalance() > self.settings.min_order_val:
                    price = auth.getTickerPrice()
                    quantity = auth.getMarginBaseAssetBalance()
                    minPricedp = self.exchangeInfo.minPricedp()
                    minQtydp = self.exchangeInfo.minQtydp()
                    price = round(price - 1 / 10 ** minPricedp, minPricedp)
                    quantity = round(quantity - 1 / 10 ** minQtydp, minQtydp)
                    log.debug_info(
                        'Sell Attempt : Pair : {}, Price : {}, Quantity : {}'.format(self.pair, price, quantity))
                    log.debug_info('********** MARKER 7 *****************')

                    try:
                        trade_details = self.settings.rest_client.create_margin_order(
                            symbol=self.pair,
                            side=self.rest_client.SIDE_SELL,
                            type=self.rest_client.ORDER_TYPE_LIMIT,
                            timeInForce=self.rest_client.TIME_IN_FORCE_GTC,
                            quantity=quantity,
                            price=str(price)
                        )
                        time.sleep(self.settings.sleep_time)
                        log.debug_info(auth.cancelMarginOrders(trade_details['orderId']))
                        time.sleep(self.settings.sleep_time)

                        try:
                            telegram_message_relay(
                                settings=self.settings,
                                telegram_message=trade_details
                            )
                            try:
                                log.debug_info('Trade ID is : {}'.format(trade_details))
                            except Exception as e:
                                log.debug_error('Catch Error : 07 : {}'.format(e))
                        except Exception as e:
                            log.debug_error('Catch Error : 08 : {}'.format(e))

                    except Exception as e:
                        log.debug_error('Catch Error : 09 : {}'.format(e))

                    while auth.getMarginBaseConvertBalance() > self.settings.min_order_val:
                        ticker_price = auth.getTickerPrice()
                        log.debug_info('Ticker Price : {}, Price : {} '.format(ticker_price, price))
                        if ticker_price != price:
                            price = auth.getTickerPrice()
                            quantity = auth.getMarginBaseAssetBalance()
                            minPricedp = self.exchangeInfo.minPricedp()
                            minQtydp = self.exchangeInfo.minQtydp()
                            price = round(price - 1 / 10 ** minPricedp, minPricedp)
                            quantity = round(quantity - 1 / 10 ** minQtydp, minQtydp)
                            log.debug_info(
                                'Sell Retrial Attempt : Pair : {}, Price : {}, Quantity : {}'.format(self.pair, price,
                                                                                                     quantity))
                            try:
                                trade_details = self.settings.rest_client.create_margin_order(
                                    symbol=self.pair,
                                    side=self.rest_client.SIDE_SELL,
                                    type=self.rest_client.ORDER_TYPE_LIMIT,
                                    timeInForce=self.rest_client.TIME_IN_FORCE_GTC,
                                    quantity=quantity,
                                    price=str(price)
                                )
                                time.sleep(self.settings.sleep_time)
                                log.debug_info(auth.cancelMarginOrders(trade_details['orderId']))
                                time.sleep(self.settings.sleep_time)

                                try:
                                    telegram_message_relay(
                                        settings=self.settings,
                                        telegram_message=trade_details
                                    )
                                    try:
                                        log.debug_info('Trade ID is : {}'.format(trade_details))
                                    except Exception as e:
                                        log.debug_error('Catch Error : 10 : {}'.format(e))
                                except Exception as e:
                                    log.debug_error('Catch Error : 11 : {}'.format(e))

                            except Exception as e:
                                log.debug_error('Catch Error : 12 : {}'.format(e))

                            time.sleep(self.settings.sleep_time)

                            if not auth.getMarginBaseConvertBalance() > self.settings.min_order_val:
                                break

                    if self.settings.marginEnabled:
                        refund = auth.refundMarginCrossLoan()
                        print(refund)

                    telegram_message = 'BINANCE SIGNAL : SELL : {} Price : {}  Time {} Australia/Sydney time ' \
                        .format(self.pair,
                                float(auth.getTickerPrice()),
                                str(datetime.now(pytz.timezone('Asia/Hong_Kong'))
                                    )
                                )
                    log.debug_info('{}'.format(telegram_message))

                    try:
                        telegram_message_relay(
                            settings=self.settings,
                            telegram_message=telegram_message
                        )
                    except Exception as e:
                        log.debug_error('Catch Error : 13 : {}'.format(e))

        if self.trade_logic.sellLogic():
            log.debug_info('We are currently short on {}'.format(self.pair))