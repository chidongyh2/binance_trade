import requests
from binance.client import Client
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'

BASE_URL = 'https://api.binance.com'
#! Binance Client init
client = Client(API_KEY, SECRET_KEY)

def getLatestCoin():
    allCoins = client.get_all_tickers()
    return allCoins[-1].get("symbol")

def getLatestCoinBUSD():
    allCoins = client.get_all_tickers()
    onlyBUSD = [""]

    #* Classifying coins(BUSD)
    for coin in allCoins:
        coinSymbol = coin.get("symbol") 
        result = check_BUSD(coinSymbol=coinSymbol) 

        if result:
            onlyBUSD.append(result)

    return onlyBUSD[-1]

#! Return Latest Coin(USDT)
def getLatestCoinUSDT():
    allCoins = client.get_all_tickers()
    onlyUSDT = [""]

    #* Classifying coins(USDT)
    for coin in allCoins:
        coinSymbol = coin.get("symbol") 
        result = check_USDT(coinSymbol=coinSymbol) 

        if result:
            onlyUSDT.append(result)

    return onlyUSDT[-1]

#! Checks for BUSD
def check_BUSD(coinSymbol): 
    busd = "BUSD"
    if busd in coinSymbol: 
        return coinSymbol  
    else:
        return False

#! Checks for USDT
def check_USDT(coinSymbol):
    usdt = "USDT"
    if usdt in coinSymbol:
        return coinSymbol
    else:
        return False