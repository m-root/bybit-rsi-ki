from bybit_client.bybit import Account
from core.round_down import round_down
from core.ticker import ticker


class Utilities():

    def __init__(self, api_key, secret_key, baseAsset, crossAsset):
        self.rest_client = Account(api_key=api_key, secret_key=secret_key)
        self.baseAsset = baseAsset
        self.crossAsset = crossAsset
        self.pair = self.baseAsset + self.crossAsset

    def getBaseAssetBalance(self):
        '''Gets the Base asset balance from the api for sell purposes'''
        account_details = self.rest_client.wallet_balance(coin=self.baseAsset)
        return float(account_details['result'][self.baseAsset]['available_balance'])

    def getCrossAssetBalance(self):
        '''Gets the Cross asset balance'''
        account_details = self.rest_client.wallet_balance(coin=self.crossAsset)
        return float(account_details['result'][self.crossAsset]['available_balance'])

    def getTickerPrice(self):
        ''' Pulls the ticker prices and returs them as an array'''
        return ticker(self.rest_client, self.pair)[0]

    def getCrossBalance(self):
        ''' Converts the cross balance in the API to the base value equivalence for buy purposes'''
        return round_down(self.getCrossAssetBalance() / self.getTickerPrice() * 0.9999, 5)

    def getCrossMinBalance(self):
        ''' Converts the cross balance in the API to the base value equivalence for buy purposes'''
        return round_down(10 / self.getTickerPrice() * 0.9999, 5)
    #
    def getCrossBalanceRaw(self):
        ''' Converts the cross balance in the API to the base value equivalence for buy purposes'''
        return round_down(self.getCrossAssetBalance() / self.getTickerPrice() * 0.999, 5)

    def getCrossBalanceConv(self, balance):
        ''' Converts the cross balance in the database to the base value equivalence for buy purposes'''
        return round_down(balance / self.getTickerPrice() * 0.999, 5)

    def getBaseConvertBalance(self):
        ''' Converts the Base balance via the API to the cross value equivalence for logic purposes'''
        return round_down(self.getBaseAssetBalance() * self.getTickerPrice() * 0.999, 2)

