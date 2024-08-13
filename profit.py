import yfinance as yf
import pandas as pd


class StockPortfolio:
    def __init__(self):
        self.stocks = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA', 'JPM', 'JNJ']

    def profit(self, start, end):
        historical_data = pd.DataFrame()
        for n in self.stocks:
            ticket = yf.Ticker(n)
            inicio = ticket.history(start=start)
            fin = ticket.history(start=end)
            dividendos = ticket.dividends[start:end].sum()
            retorno = (fin['Close'].values[0] + dividendos - inicio['Close'].values[0]) / inicio['Close'].values[0]
            retorno = retorno * 100
            # print(f'{n} start Price:{round(inicio["Close"].values[0], 2)} - end Price{round(fin["Close"].values[0],2)} - Profit: {round(fin["Close"].values[0],2) - round(inicio["Close"].values[0], 2)}')
            historical_data[n] = {'start_price': round(inicio['Close'].values[0], 2),
                                  'end_price': round(fin['Close'].values[0], 2),
                                  'profit': round(fin['Close'].values[0], 2) - round(inicio['Close'].values[0], 2),
                                  'dividendos': dividendos,
                                  'retorno': round(retorno,2)}
        print(historical_data.head())

    def price(self, stock, date):
        ticket = yf.Ticker(stock)
        precio = ticket.history(start=date)
        precio = precio['Close'].values[0]

        return round(precio,2)


portfolio = StockPortfolio()

portfolio.profit("2023-01-01", "2024-01-01")
print(portfolio.price('AAPL', "2024-01-01"))
