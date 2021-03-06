import numpy as np
import pandas as pd
from manage_list import tools
from init import config

def cross_check_data(df):
    len_symbols = len(df)
    df_database = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA)
    list_data_symbols = df_database['symbol'].to_list()
    list_df_symbols = df['symbol'].to_list()
    df = df.set_index('symbol',drop=True)

    for ticker in list_data_symbols:
        if ticker in list_df_symbols:
            try:
                df = df.drop(index=ticker)
                #print(ticker)
            except:
                pass

    df['symbol'] = df.index
    df.reset_index(drop=True, inplace=True)
    df = tools.move_column_position(df, 'symbol', 0)
    df = tools.clean_up_df_column(df)

    print('-> already in database: ', len_symbols - len(df))
    print('-> remaining symbols: ',len(df))

    return df


def check_valid_data(df):
    df = df.replace(r'^\s+$', np.nan, regex=True)
    df = df.dropna()

    return df

