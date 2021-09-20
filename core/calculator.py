from m_run.novatron import settings
from core.ticker import ticker
from numpy import mean
#TODO

'''
[d for d in list(settings.rest_client.my_trades(symbol="BTCUSDT")) if len(settings.rest_client.my_trades(symbol="BTCUSDT"))>0]
'''

def curr():
    return [list(d.values()) for d in settings.private_auth.balance()]

def current_price(pair):
    return float(round(mean(ticker(pair)[1:]),5))

def current_ask_price(pair):
    return float(ticker(pair)[1])

def current_bid_price(pair):
    return float(ticker(pair)[2])

# def take_rate(pair):
#     return float(settings.private_auth.trading_commission("BTCUSD")['takeLiquidityRate'])
#
# def provide_rate(pair):
#     return float(settings.private_auth.trading_commission("BTCUSD")['provideLiquidityRate'])
#
# def get_base(pair):
#     balance = curr()
#     for f in balance:
#         if 'BTC' in f:
#             base = balance[balance.index(f)][1]
#     return float(base)
#
# def get_cross(pair):
#     balance = curr()
#     for f in balance:
#         if 'USD' in f:
#             cross = balance[balance.index(f)][1]
#     return float(cross)
#
# def cross_amount(pair):
#     return (get_cross()-(provide_rate()*(current_price())))/current_price()
#
# print(get_cross()/current_bid_price())
# print(get_base())
# print()