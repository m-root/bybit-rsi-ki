from bybit_client.bybit import Account
api_key = 'a1ZsHxHBbqYjVkzRnq'
secret_key = 'QMm9cgo474u3X3svTOS87PFb9VJprJlrBwRJ'

client  = Account( api_key=api_key, secret_key=secret_key)

symbol="BTCUSD"

from core import ticker
print(ticker.ticker(symbol, client))
# print(client.Kline(symbol="BTCUSD").result())

# APIkey, Common, Conditional, Execution, Funding, Kline, Market, Order, Positions, Symbol, Wallet

# Get server time
'''
<class 'list'>: 
<class 'dict'>: {'$ref': '#/definitions/KlineBase', 'x-scope': ['https://api-testnet.bybit.com/doc/swagger.txt']}
[{'name': 'symbol', 'in': 'query', 'description': 'Contract type.', 'required': True, 'type': 'string'}, 
{'name': 'interval', 'in': 'query', 'description': 'Kline interval.', 'required': True, 'type': 'string'}, 
{'name': 'from', 'in': 'query', 'description': 'from timestamp.', 'required': True, 'type': 'number', 'format': 'int64'}, 
{'name': 'limit', 'in': 'query', 'description': 'Contract type.', 'required': False, 'type': 'string'}]
'''

# print(client.Kline.kline_get())

# # Get Symbol lists
# print(client.Symbol.Symbol_get().result()[0]["result"][0])
#
# # Change account user leverage
# print(client.Positions.Positions_saveLeverage(symbol="BTCUSD", leverage="14").result())
#
# # Query account positions
# print(client.Positions.Positions_myPosition().result())
#
# #Place an Active Order
# print(client.Order.Order_new(side="Buy",symbol="BTCUSD",order_type="Limit",qty=1,price=8300,time_in_force="GoodTillCancel").result())
#
# #Get Active Order
# print(client.Order.Order_getOrders().result())
#
# #Cancel Active Order
# print(client.Order.Order_cancel(order_id="baaa9182-86e1-42aa-8420-da6428346b30").result())
#
# # Place Conditional Order
# print(client.Conditional.Conditional_new(order_type="Limit",side="Buy",symbol="BTCUSD",qty=1,price=8100,base_price=8300,stop_px=8150,time_in_force="GoodTillCancel").result())
#
# #Get Conditional Order
# print(client.Conditional.Conditional_getOrders().result())
#
# #Cancel conditional order
# print(client.Conditional.Conditional_cancel(stop_order_id="53c8e250-252b-47f7-a768-5f5456b64e17").result())
#
# #changeMargin
# print(client.Positions.Positions_changeMargin(symbol="BTCUSD", margin="10").result())
#
# #Set Trading-Stop
# print(client.Positions.Positions_tradingStop(symbol="BTCUSD",stop_loss="8100").result())
#
# #Get wallet fund records
# print(client.Wallet.Wallet_getRecords().result())
#
# #Get the Last Funding Rate
# print(client.Funding.Funding_predictedRate(symbol="BTCUSD").result())
#
# #Get My Last Funding Fee
# print(client.Funding.Funding_getRate(symbol="BTCUSD").result())
#
# #Get Predicted Funding Rate and Funding Fee
# print(client.Funding.Funding_predicted(symbol="BTCUSD").result())
#
# #Get the trade records of a order
# print(client.Execution.Execution_getTrades(order_id="24d6c1b1-e2aa-4ef0-8d73-55b751710a0c").result())
#
# #Get Orderbook
# print(client.Market.Market_orderbook(symbol="BTCUSD").result())
#
# #market symbol info
# print(client.Market.Market_symbolInfo(symbol="BTCUSD").result())
#
# #Latest information for symbol
# print(client.Market.Market_symbolInfo().result())
