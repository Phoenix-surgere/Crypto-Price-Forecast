# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:09:31 2021

@author: black
"""

import re
import pandas as pd


def ts_range(crypto_data, currency_id, details):
  '''
  Accepts index b/c particularly easy to loop and get for all curencies. Could
  easiy be modified to accept currency name itself but that may be easy to trip user up
  '''
  coin = crypto_data[crypto_data["Asset_ID"]==currency_id]
  start = coin.head(1).index[0]
  end = coin.tail(1).index[0]
  res = details.loc[details.Asset_ID == currency_id, 'Asset_Name'].to_string()
  res = re.split( "\d", res)[-1].lstrip()
  print(f"""{res} goes from {start.year}-{start.month}-{start.day} to """
    f"""{end.year}-{end.month}-{end.day}""")
  
  
def handle_na_index(crypto_coin_df):
  init_na = (crypto_coin_df.index[1:]-crypto_coin_df.index[:-1]).value_counts()
  print(f"Initial na values (missing index rows): \n {init_na} \n ")
  date_range = pd.date_range(crypto_coin_df.index[0], crypto_coin_df.index[-1], freq="min")
  reindexed_df = crypto_coin_df.reindex(date_range, method='pad' )
  clean_na = (reindexed_df.index[1:]-reindexed_df.index[:-1]).value_counts()
  print(f"After cleaning na values (missing index rows): \n {clean_na}")
  return reindexed_df