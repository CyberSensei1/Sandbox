# -*- coding: UTF-8 -*-
import urllib
import pandas
import trendy
from roughsr2 import find_support, find_resistance
import matplotlib.pyplot as plt

url = 'https://www.binance.com/api/v1/klines?symbol=BTCUSDT&interval=2h'
response = urllib.urlopen(url) 
df = pandas.read_json(response.read()) 
df=df.tail(100) #Son 100 mum alınıyor
x=df[4] #Close değerleri alınıyor
resis=find_resistance(x)
sup=find_support(x)

result = trendy.gentrends(x, window = 1.0/3, charts = False) 
# Trendler hesaplanıyor charts =False ile kendi kütüphanesindeki chart kullanılmaması sağlanıyor

plt.plot(result[0])
for xr in resis:
    plt.axhline(y=xr, color='r', linestyle='--', label='Direnc')
for xs in sup:
    plt.axhline(y=xs, color='g', linestyle='--', label='Destek')
plt.ylabel('Fiyat')
plt.xlabel('Son Mum Sayisi')
plt.show()
