import telegram
from binance.client import Client

##########################################################
#########                API DETAILS            ##########
##########################################################
api_key = 'snMGybC5HRPCWYFN5CS4zkjMEiKcjKgstoLq7z54VNiQeGrdQU29gMOTxfmJGR4x'
secret_key = 'tX0uh8sJ7oFYJ6osIc07Df39MtdfNi2psgpGZA4ooQlBg0wc4OysLbLJj0Ry6Rzd'
requests_params=None
rest_client = Client(api_key, secret_key, requests_params)

##########################################################
#########              TRADE DETAILS            ##########
##########################################################
trade = True
marginEnabled = True
min_order_val = 10
sleep_time = 2

##########################################################
#########                HA SETTINGS            ##########
##########################################################
period='15m'
firstSmooth = 178
rateSmooth = 5

##########################################################
#########              TELEGRAM SETTINGS            ##########
##########################################################
chat_id = "-282619797"
bot = telegram.Bot(token='620369180:AAF58K-FUyB1E5L-AwEdp6D7GFciRNxEYJw')

##########################################################
#########              TELEGRAM SETTINGS            ##########
##########################################################
chat_id = "-1001278609479"
bot = telegram.Bot(token='620369180:AAF58K-FUyB1E5L-AwEdp6D7GFciRNxEYJw')


