import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from stock import get_data
import pandas as pd
from series_cont import get_cont
import pickle

#x,y = get_cont("facebook")
#pickle.dump((x,y), open("fb", "wb"))
x,y = pickle.load(open("fb","rb"))
stock_data = get_data("FB")

#stock_data['diff'] = stock_data['Close'] - stock_data['Close'].shift(-1)
stock_data['diff'] = stock_data['Close'].diff().abs()
stock_data['Controversy'] = pd.Series(y, index=x)
print(stock_data)


#stock_data[["Close"]].plot(title="Facebook Stock Price vs Controversy")
stock_data[['Controversy']].plot()
stock_data[['Controversy','diff']].plot(secondary_y='Controversy')


plt.show()