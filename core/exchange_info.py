# import time
# import requests
# import decimal
#
# BASE_URL = 'https://www.binance.com/api/v1/exchangeInfo'
#
#
# class ExchangeInfo():
#
#     def __init__(self, pair):
#         self.pair = pair
#
#     def simple_request(self, url):
#         r = requests.get(url)
#         if r.status_code == 200:
#             return r.json()
#         else:
#             return self.simple_request_again(url)
#
#     def simple_request_again(self, url):
#         time.sleep(0.5)
#         r = requests.get(url)
#         return r.json()
#
#     def find_exchange_info(self, symbol):
#         full_lists = self.simple_request(BASE_URL)
#         a = full_lists['symbols']
#         for i in a:
#             if i['symbol'] == symbol:
#                 return i
#             else:
#                 pass
#
#     def minQtydp(self):
#         f = self.find_exchange_info(self.pair)
#         return -decimal.Decimal(
#             str(float([d['minQty'] for d in f['filters'] if d['filterType'] == 'LOT_SIZE'][0]))).as_tuple().exponent
#
#     def minPricedp(self):
#         f = self.find_exchange_info(self.pair)
#         return -decimal.Decimal(str(
#             float([d['minPrice'] for d in f['filters'] if d['filterType'] == 'PRICE_FILTER'][0]))).as_tuple().exponent
#
#     def minAmount(self):
#         f = self.find_exchange_info(self.pair)
#         return float([d['minQty'] for d in f['filters'] if d['filterType'] == 'LOT_SIZE'][0])
#
#     def maxAmount(self):
#         f = self.find_exchange_info(self.pair)
#         return float([d['maxQty'] for d in f['filters'] if d['filterType'] == 'LOT_SIZE'][0])
#
#     def baseAsset(self):
#         f = self.find_exchange_info(self.pair)
#         return f['baseAsset']
#
#     def quoteAsset(self):
#         f = self.find_exchange_info(self.pair)
#         return f['quoteAsset']
