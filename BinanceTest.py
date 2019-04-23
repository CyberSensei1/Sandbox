# coding=utf-8
import urllib
import pandas
import matplotlib.pyplot as pyplot
from stockstats import StockDataFrame

#Binance api üzerinden istenilen coinin datasını çekeceğiz.
url = 'https://www.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1d'
names = ['Opentime','Open','High','Low','Close','Volume','Closetime','Quoteassetvolume','Numberoftrades','Takerbuybaseassetvolume','Takerbuyquoteassetvolume','Ignore']
response = urllib.urlopen(url)

df =pandas.read_json(response.read())

#Daha sonra çekilen bu datayı bilgisyara kaydedeceğiz.
df.to_csv('BinanceTest.csv', encoding='utf-8', index=False, header=False)

#Kaydedilen datanın grafiği çizilecek
dataframe = pandas.read_csv('BinanceTest.csv', names=names)

#MACD SMA RSI gibi hesaplamalar yapılacak.
stock = StockDataFrame.retype(dataframe)
rsi12 = stock['rsi_12']

dataframe.opentime= pandas.to_datetime(dataframe.opentime, unit='ms')

pyplot.subplot(211)
pyplot.title('BTC-USDT')
pyplot.plot(dataframe.opentime, dataframe.close)
#Grafiği bu hesaplamalar eklenecek.
pyplot.subplot(212)
pyplot.title('RSI-12')
pyplot.plot(dataframe.opentime, rsi12)
pyplot.show()
