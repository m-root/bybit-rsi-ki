# import telegram
from bybit_client.bybit import Account

api_key = 'a1ZsHxHBbqYjVkzRnq'
secret_key = 'QMm9cgo474u3X3svTOS87PFb9VJprJlrBwRJ'
leverage=1

rest_client = Account(api_key, secret_key,leverage)

# chat_id = "-1001238068408"
# bot = telegram.Bot(token='620369180:AAF58K-FUyB1E5L-AwEdp6D7GFciRNxEYJw')


break_even_after = 35
tracker = 20
stop_loss = 35
limit=100


############################ RSI SETTINGS ######################################

buy_rsi = 31
sell_rsi = 69
rsi_period = 30
rsi_interval = '15m'

############################ KI SETTINGS ######################################


mkb_period = 30
mkb_interval = '15m'

# print(rest_client.get_wallet_fund_records())

############################ LONG SETTINGS ######################################
longCrosslevel = 31



firstOffSet = 0.7
secondOffSet = 0.3
thirdOffSet = 0.1