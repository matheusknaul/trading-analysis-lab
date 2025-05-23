import yfinance as yf
import mysql.connector
from datetime import datetime
import pandas as pd
from datetime import datetime

def search_carteira():
    pass
def insert_carteiras(df):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='bolsa'
    )
    cursor = conn.cursor()

    #lógica

    conn.commit()
    cursor.close()
    conn.close()

    print(f'Carteiras inseridas com sucesso!')

def insert_carteira(register):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='bolsa'
    )
    cursor = conn.cursor()

    sql = """
        INSERT INTO carteiras(
            ticker, nome, tipo, qtd_teorica, part_percentage
        ) VALUES(%s, %s, %s, %s, %s)
    """
    valores = (register[0], register[1], register[2], register[3], register[4])
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()

    carteira = ""
    print(f'Dados de {carteira} salvos com sucesso!')

def insert_rows(df, timeframe, nome_acao):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='bolsa'
    )
    cursor = conn.cursor()

    ticker_main = ""
    for _, row in df.iterrows():
        sql = """
            INSERT INTO candles(
                ticker, timeframe, datetime, open, high, low, close, volume
            ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
        """

        data_datetime = row['Date']
        if hasattr(data_datetime, 'to_pydatetime'):
            data_datetime = data_datetime.to_pydatetime()

        valores = (
            row['Ticker'], 
            timeframe, 
            data_datetime, 
            row[f'Open_{nome_acao}'], 
            row[f'High_{nome_acao}'], 
            row[f'Low_{nome_acao}'], 
            row[f'Close_{nome_acao}'], 
            row[f'Volume_{nome_acao}']
        )
        ticker_main = row['Ticker']
        cursor.execute(sql, valores)

    conn.commit()
    cursor.close()
    conn.close()

    print(f'Dados de {ticker_main} salvos com sucesso!')
