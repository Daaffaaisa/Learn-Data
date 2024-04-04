#Line Chart digunakan untuk menggambarkan tren nilai daeri suatu variabel terhadap variabel lain

import matplotlib.pyplot as plt

lemon_dm = [6.44, 6.87, 7.7, 8.85, 8.15, 
                  9.96, 7.21, 10.04, 10.2, 11.06]
lemon_weight = [112.05, 114.58, 116.71, 117.4, 128.93, 
                132.93, 138.92, 145.98, 148.44, 152.81]

plt.plot(lemon_dm, lemon_weight)
plt.show()

#Implementasi menggunakan kode saham BBCA
import pandas as pd

url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'
df = pd.read_csv(url)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Close'], color='green')
plt.xlabel('Date', size = 15)
plt.ylabel('Price', size = 15)
plt.show()