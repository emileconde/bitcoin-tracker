import requests
import apikey
from bitcoin import Bitcoin


def get_json():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': apikey.get_api_key()
    }

    params = {
        'start': '1',
        'limit': '5',
        'convert': 'USD'
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    return requests.get(url, params=params, headers=headers).json()


def parse_json(response):
    bitcoins = response['data']
    bitcoin_dict = {}
    index = 1
    for bitcoin in bitcoins:
        name = bitcoin['name']
        symbol = bitcoin['symbol']
        price = bitcoin['quote']['USD']['price']
        last_updated = bitcoin['quote']['USD']['last_updated']
        bitcoinObject = Bitcoin(name, symbol, price, last_updated)
        bitcoin_dict[index] = [bitcoinObject.name, bitcoinObject.symbol,
                               bitcoinObject.price, bitcoinObject.last_updated]
        index = index + 1
    return bitcoin_dict
