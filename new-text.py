import yfinance as yf
import pandas as pd


nome_acao = "ITUB4.SA"

# Baixa os dados do pregão anterior (19/05)
df = yf.download(nome_acao, start="2024-05-18", end="2025-05-20", interval="1m")

print(df)