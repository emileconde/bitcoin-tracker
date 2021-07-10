from utils import*

response = get_json()
bitcoin_dict = parse_json(None)

if bitcoin_dict is not None:
    dataframe = build_dataframe(bitcoin_dict)

if dataframe is not None:
    build_db_from_dataframe(dataframe)
