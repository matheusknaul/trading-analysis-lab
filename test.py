import yfinance as yf
import pandas as pd
from mysql_connection import insert_rows

nome_acao = "ITUB4.SA"
timeframe = '1d'

# Baixa os dados do pregão anterior (19/05)
df = yf.download(nome_acao, start="2005-05-22", end="2025-05-22", interval=timeframe)
df.reset_index(inplace=True)

#achatar
if isinstance(df.columns, pd.MultiIndex):
    df.columns = ['_'.join(filter(None, col)).strip() for col in df.columns.values]

df['Ticker'] = nome_acao

print(df.columns)
print(df.head())

insert_rows(df, timeframe, nome_acao)

