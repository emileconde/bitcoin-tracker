import pandas as pd
import requests
import apikey
from bitcoin import Bitcoin
from sqlalchemy import create_engine


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
    if response is None:
      return "There seems to be an empty response"
    
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

  
def build_dataframe(bit_dict):
    # Converting the dictionary into a dataframe
    bit_dict = pd.DataFrame.from_dict(bit_dict, orient='index',
                                   columns=['name', 'symbol',
                                            'price', 'last_updated'])
    return bit_dict

    
def build_db_from_dataframe(dframe):
    # Create engine
    engine = create_engine('mysql://root:codio@localhost/bitcoin_db')
    dframe.to_sql('bitcoin_table', con=engine, if_exists='replace', index=False)
