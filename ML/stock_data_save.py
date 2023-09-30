import yfinance as yf
import numpy as np

# Big Tech
tickers = [ "AAPL", "TSLA", "MSFT", "AMZN", "GOOG", "NVDA", "PYPL", "INTC", "ADBE" ]
colums = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

data = yf.download(tickers, period="730d", interval="1h", group_by="ticker")

data.to_csv("stock_data.csv")


chart = {}
# load data from csv
for i in range(0, len(tickers)):
    stock_data = np.loadtxt("stock_data.csv", delimiter=",", skiprows=3, usecols=(i*6+1, i*6+2, i*6+3, i*6+4, i*6+5, i*6+6))
    max_close = np.max(stock_data[:,3])
    chart[tickers[i]] = stock_data

data_shape = chart[tickers[0]].shape
print(chart)

INPUT_SIZE = 50
OUTPUT_SIZE = 3

training_data = []

for k, v in chart.items():
  train_input_data = np.array([v[i:i+INPUT_SIZE] for i in range(0, len(v)-INPUT_SIZE-OUTPUT_SIZE)])
  train_output_data = np.array([v[i+INPUT_SIZE:i+INPUT_SIZE+OUTPUT_SIZE,3] for i in range(0, len(v)-INPUT_SIZE-OUTPUT_SIZE)])