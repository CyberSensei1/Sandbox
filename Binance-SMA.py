#https://twitter.com/SenseiCyber
import urllib
import pandas
import matplotlib.pyplot as pyplot
from stockstats import StockDataFrame

url = 'https://www.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1d'
#Binance api adresi symbol= den sonra istediğiniz sembol ü yazabilirsiniz.
#interval= dan sonrada istediğiniz zaman dilimi 1d,4h,15m gibi


names=['Opentime','Open','High','Low','Close','Volume','Closetime','Quoteassetvolume','Numberoftrades',
       'Takerbuybaseassetvolume','Takerbuyquoteassetvolume','Ignore']
#Gelen kolonların isimleri binance yeni kolon eklemediği sürece değiştirilmesine gerek yok.


response = urllib.urlopen(url) #Binance api linkine istek atıyoruz.
df = pandas.read_json(response.read()) #dönen response u okuyup pandas datayapısına alıyoruz.

df.to_csv('BinanceTest.csv', encoding='utf-8', index=False, header=False)#CSV dosyası olarak kaydediyoruz.

dataframe = pandas.read_csv('BinanceTest.csv', names=names) #CSV deki dataları kolon isimleri ile alıyoruz.


stock = StockDataFrame.retype(dataframe) #stockstats kütüphanesinin hesaplamaları için gerekli veri tipine dönüştürüyoruz.
calc=stock.get('close_50_sma') #kapanış fiyatına göre SMA 50 hesaplanıyor
calc2=stock.get('close_20_sma') #kapanış fiyatına göre SMA 20 hesaplanıyor

dataframe.opentime=pandas.to_datetime(dataframe.opentime,unit='ms') #Binance linux timestamp gönderiyor zamanı bunu düzgün zaman yapısına çeviriyoruz.

pyplot.subplot(211)
pyplot.title('BTC-USD')
pyplot.plot(dataframe.opentime,dataframe.close)
#İstediğimiz paritenin kapanış fiyatına göre çizdiriyoruz.


pyplot.subplot(212)
pyplot.title('SMA(50)-SMA(20)')
pyplot.plot(dataframe.opentime, calc,dataframe.opentime,calc2)
pyplot.show()
#hesaplanan SMA50 ve SMA20 değerlerini çizdiriyoruz.

