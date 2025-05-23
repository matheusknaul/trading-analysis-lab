import yfinance as yf
import mysql.connector
from datetime import datetime
import pandas_ta as ta
from datetime import datetime

def insert_rows(list):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='bolsa'
    )

    cursor = conn.cursor()

    ticker_main = ""
    for _, row in list.iterrows():
        sql = """
            INSERT INTO candles(
                ticker, timeframe, datetime, open, high, low, close, volume
            ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            """
        valores = (
            row['ticket'], row['timeframe'], row['datetime'].to_pydatetime(), row['open'], 
            row['high'], row['low'], row['close'], row['volume']
        )
        ticker_main = row['ticket']
        cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()

    print(f'Dados de {ticker_main} salvos com sucesso!')