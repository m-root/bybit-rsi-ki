from m_run.novatron import settings
from core import calculator, candle
from core import ticker

from pyti import average_true_range as atr

class Trails(object):

    def __init__(self, pair="BTCUSD"):
        self.base = 'BTC'
        self.cross = 'USD'
        self.pair = pair
        self.buy_entry = []
        self.buy_exit = []
        self.sell_entry = []
        self.sell_exit = []
        self.pending_buy_orders = []
        self.pending_sell_orders = []
        self.atr_data = atr.average_true_range(
            close_data=self.candle[3],
            period=settings.atr_period
        )

        self.time_frame = "15m"
        self.limit = settings.limit
        self.candle = candle.candles(symbol=self.pair, interval=self.time_frame)

    auth = settings.rest_client
    auth.my_trades()

    def sell_trail(self):
        return float(ticker.ticker(self.pair)[1]) - min((self.atr_data[-1], settings.entry_atr_period)[-(
                settings.entry_atr_period + 2):-2])

    def buy_trail(self):
        return float(ticker.ticker(self.pair)[2]) + float(settings.stop_loss)

    def sell_trail_list(self):
        if len(self.sell_exit) == 0 or Trails().buy_trail() < self.sell_exit[-1]:
            self.sell_exit.append(Trails().buy_trail())
        return self.sell_exit


    def buy_trail_list(self):
        if len(self.buy_exit) == 0 or Trails().sell_trail() > self.buy_exit[-1]:
            self.buy_exit.append(Trails().sell_trail())
        return self.buy_exit


    def trailing(self):
        trails = [d for d in list(settings.rest_client.my_trades(symbol=self.pair)) if len(
            settings.rest_client.my_trades(symbol=self.pair)) > 0]

        price = float(trails[6])
        print(trails)
        # if len(tra)
        if trails[4] == 'buy':
            self.buy_trail()

            if len(self.pending_buy_orders) <= 0 :
                stop_loss = price - settings.stop_loss
                # self.buy_exit.append(stop_loss)
                if len(self.sell_exit) > 0:
                    del self.sell_exit[:]
                    pending = settings.private_auth.new_order(tpair=self.pair, side='sell', quantity=calculator.get_base(),
                                                              price=stop_loss, trade_type='limit')
                    self.pending_buy_orders.append(pending['id'])


            if float(auth.active_order()[0]['price']) > float(self.buy_exit[-1]):
                last_buy_trail = self.buy_trail()
                auth.cancel_order(orderData=self.pending_buy_orders[-1])
                order_data = auth.new_order(tpair=self.pair, side='sell', quantity=calculator.get_base(),
                                                price=last_buy_trail, trade_type='limit')

                self.pending_buy_orders.append(order_data['id'])
                print(last_buy_trail)
            if float(settings.public_auth.ticker(tpair=self.pair)['last']) >= settings.break_even_after + price:
                settings.private_auth.cancel_orders(tpair=self.pair)
                settings.private_auth.new_order(tpair=self.pair, side='sell', quantity=calculator.get_base(),
                                                price=price, trade_type='limit')




        if trails[4] == 'sell':
            stop_loss = price + settings.stop_loss
            if len(self.sell_exit) <= 0:
                self.sell_exit.append(stop_loss)
                if len(self.buy_exit)>0:
                    del self.buy_exit[:]
                print(settings.private_auth.new_order(tpair=self.pair, side='buy', quantity=calculator.get_cross() / calculator.current_bid_price(),
                                                      price=stop_loss, trade_type='limit'))

            if self.sell_trail() > self.sell_exit[-1]:
                last_sell_trail = self.sell_trail()
                settings.private_auth.cancel_orders(tpair=self.pair)
                settings.private_auth.new_order(tpair=self.pair, side='buy', quantity=calculator.get_cross() / calculator.current_bid_price(),
                                                price=stop_loss, trade_type='limit')


            if float(settings.public_auth.ticker(tpair=self.pair)['last']) <= price - settings.break_even_after:
                settings.private_auth.cancel_orders(tpair=self.pair)
                quantity = calculator.get_cross()/calculator.current_bid_price()
                print('Quantity is {}'.format(quantity))
                settings.private_auth.new_order(tpair=self.pair, side='buy', quantity=quantity,
                                                price=stop_loss, trade_type='limit')





import time

trails = Trails()
def main():


    while True:
        try:
            print('+++++++++++++++++++++ BUY TRAILS ++++++++++++++++++++++')
            print()
            print(trails.buy_exit)
            print('+++++++++++++++++++++ SELL TRAILS ++++++++++++++++++++++')
            print()
            print(trails.sell_exit)


        except Exception as e:
            print(e)
            time.sleep(3)


if __name__ == '__main__':
    main()
