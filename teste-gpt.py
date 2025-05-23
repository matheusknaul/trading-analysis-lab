import yfinance as yf
import pandas as pd


nome_acao = "ITUB4.SA"

# Baixa os dados do pregão anterior (19/05)
df = yf.download(nome_acao, start="2025-05-18", end="2025-05-20", interval="1m")

# Preço de fechamento do dia 19/05
close_prev = df['Close'].iloc[0]
print("Fechamento 19/05: ", close_prev[nome_acao])

df['Price Change %'] = ((df['Close'] / close_prev) - 1) * 100

print(df)
