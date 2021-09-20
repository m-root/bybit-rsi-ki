import numpy

from core import log, ticker, candle
from pyti import relative_strength_index as rsi, keltner_bands as ki


class TradingLogic:

    def __init__(self, pair, period, tFrame, settings):
        self.pair = pair
        self.period = period
        self.tFrame = tFrame
        self.settings = settings

    def buyLogic(self):

        data = candle.candles(symbol=self.pair, interval=self.tFrame, rest_client=self.settings.rest_client)
        rsiLogic = rsi.relative_strength_index(data=data, period=self.period)[-2] > self.settings.buy_rsi
        kcPriceUnderLogic = \
        ki.center_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[
            -3] > ticker.ticker(self.settings.rest_client, pair=self.pair) and rsiLogic
        kcPriceOverLogic = \
        ki.center_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[
            -2] < ticker.ticker(self.settings.rest_client, pair=self.pair) and rsiLogic

        log.debug_info('Price Under trade_logic is : %s  ' % (kcPriceUnderLogic))
        log.debug_info('Price Over trade_logic is : %s  ' % (kcPriceOverLogic))

        if kcPriceUnderLogic:
            '''if price is below mid_KC enter in the next candle'''
            return [True, ticker.ticker(self.settings.rest_client, pair=self.pair)]

        elif kcPriceOverLogic:
            '''if price>mid_KC then place buy limit at mid_kc and update price'''

            return [True,
                    ki.center_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[
                        -2]]

        else:
            return False

    def buyStopLoss(self):

        data = candle.candles(symbol=self.pair, interval=self.tFrame, rest_client=self.settings.rest_client)
        '''

        stop_loss = Lowest_price in 48 candles - 15
            if stop_loss > Entry_price
        stop_loss - 150

        :return: 
        '''
        if (numpy.amin(data) - 15) > ticker.ticker(self.settings.rest_client, pair=self.pair):
            return numpy.amin(data) - 15

        else:
            return ticker.ticker(self.settings.rest_client, pair=self.pair) - 150

    def sellLogic(self):

        data = candle.candles(symbol=self.pair, interval=self.tFrame, rest_client=self.settings.rest_client)
        rsiLogic = rsi.relative_strength_index(data=data, period=self.period)[-2] < self.settings.sell_rsi
        kcPriceOverLogic = \
        ki.center_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[
            -3] < ticker.ticker(
            self.settings.rest_client, pair=self.pair) and rsiLogic
        kcPriceUnderLogic = \
        ki.center_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[
            -2] > ticker.ticker(
            self.settings.rest_client, pair=self.pair) and rsiLogic

        log.debug_info('Price Over trade_logic is : %s  ' % (kcPriceUnderLogic))
        log.debug_info('Price Under trade_logic is : %s  ' % (kcPriceOverLogic))

        if kcPriceUnderLogic:
            '''if price is below mid_KC enter in the next candle'''
            return [True, ticker.ticker(self.settings.rest_client, pair=self.pair)]

        elif kcPriceOverLogic:
            '''if price>mid_KC then place buy limit at mid_kc and update price'''

            return [True,
                    ki.center_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[
                        -2]]

        else:
            return False

    def sellStopLoss(self):
        data = candle.candles(symbol=self.pair, interval=self.tFrame, rest_client=self.settings.rest_client)
        '''

        stop_loss = Lowest_price in 48 candles - 15
            if stop_loss > Entry_price
        stop_loss - 150

        :return: 
        '''
        if (numpy.amax(data) + 15) < ticker.ticker(self.settings.rest_client, pair=self.pair):
            return numpy.amax(data) + 15

        else:
            return ticker.ticker(self.settings.rest_client, pair=self.pair) + 150

    def buyTakeProfit(self):
        '''
        P1A
        if entry kcPriceUnderLogic TP = entry+10 and 70% off the market
        P1B
        if entry kcPriceOverLogic TP =  (Upper Keltner - Mid Keltner Basis)/4 + Entry Price and  70% off the market

        P2
        (Upper Keltner - Mid Keltner Basis)/2 + Entry Price and  70% off the market
        ***After Profit Target 2 hit move stop price to breakeven**

        P3
        When Lower Keltner line is higher than break even stop price move stop every
        period (1 hour) until stopped out. Stop can only move up not down.

        if lkc > Entry_price
            new_tp = lkc
        '''
        data = candle.candles(symbol=self.pair, interval=self.tFrame, rest_client=self.settings.rest_client)
        upperKeltner = \
        ki.upper_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[-2]
        midKeltner = \
        ki.center_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[-2]
        lowerKeltner = \
        ki.lower_band(close_data=data[0], high_data=data[1], low_data=data[2], period=self.settings.mkb_period)[-2]
        if ticker.ticker(self.settings.rest_client, pair=self.pair) >= self.entryPrice + self.firstTarget:
            offset = self.settings.firstOffSet
            '''market_close for P1A'''
            return offset

        if ticker.ticker(self.settings.rest_client, pair=self.pair) >= (upperKeltner - midKeltner) / 4 + self.entryPrice:
            offset = self.settings.firstOffSet
            '''market_close for P1B'''
            return offset

        if ticker.ticker(self.settings.rest_client, pair=self.pair) >= (upperKeltner - midKeltner) / 2 + self.entryPrice:
            offset = self.settings.secondOffSet
            '''market_close for P2 Update API for Change of  stop loss to BE'''
            return [offset, self.entryPrice]  # entryPrice for breakEven

        if lowerKeltner >= self.entryPrice:
            '''Update the trail stop every cycle upon refresh '''
            return lowerKeltner


