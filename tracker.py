import pandas as pd
from utils import get_json
from utils import parse_json
from sqlalchemy import create_engine

# Getting and parsing JSON
response = get_json()
bitcoin_dict = parse_json(response)


# Converting the dictionary into a dataframe
dataframe = pd.DataFrame.from_dict(bitcoin_dict, orient='index',
                                   columns=['name', 'symbol',
                                            'price', 'last_updated'])

print(dataframe)

# Create engine
engine =
create_engine('mysql://root:codio@localhost/bitcoin_db')
dataframe.to_sql('bitcoin_table', con=engine, if_exists='replace', index=False)
