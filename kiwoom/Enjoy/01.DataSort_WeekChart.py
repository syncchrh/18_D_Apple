#-*- coding: utf-8 -*-
import csv
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# #Pandas 자료형으로 변환
#data = DataFrame(raw_data, columns=['code', 'name', 'volume', 'currentPrice', 'PER', 'EPS', 'ROE', 'PBR', 'EV', 'BPS', 'salesAccount', 'operatingProfit', 'perProfit', 'total'])
# #data = DataFrame(raw_data)
#
# print(data.ix['20180319'])
#
# #np.save('test',data)
# print(data)
# newDF = DataFrame()
# newDF = newDF.append(data, ignore_index=True)

#data = data.sort_values(by='total', ascending=True)
#data.sort_values(by="PBR")


dataName = 'day'
index = ['CurrentPrice', 'Volume', 'TradingValue', 'Date', 'StartPrice', 'HighPrice', 'LowPrice', 'a', 'b', 'c', 'd', 'e', 'f', 'h']
df = pd.read_csv("E:\99.Coding\\18_D_Apple\Data\csv\\" + dataName + "data_018000.csv", names=index)
df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y%m%d') #Date -> Datetime 변환
df = df.set_index("Date")
print(df)
#df.CurrentPrice = pd.to_numeric(df.CurrentPrice, errors='coerce')
#df.CurrentPrice = pd.to_numeric(df.CurrentPrice, errors='coerce').fillna(0).astype(np.int64)


#df = df.sort_values(by='Date', ascending=True)



#print(df)

#print(df)
# dataPER = df.sort_values(by='PER', ascending=True)
# dataEPS = df.sort_values(by='EPS', ascending=False)
# dataROE = df.sort_values(by='ROE', ascending=False)
# dataPBR = df.sort_values(by='PBR', ascending=True)
# dataEV = df.sort_values(by='EV', ascending=False)
# dataBPS = df.sort_values(by='BPS', ascending=False)
#
# kind = 'kosdaq'

#Pandas 데이터 저장
# dataPER.to_csv("E:\99.Coding\\18_D_Apple\Data\csv\\sort\\" + kind + "\\PER.csv", encoding='utf-8', mode='w', header=False)
# dataEPS.to_csv("E:\99.Coding\\18_D_Apple\Data\csv\\sort\\" + kind + "\\EPS.csv", encoding='utf-8', mode='w', header=False)
# dataROE.to_csv("E:\99.Coding\\18_D_Apple\Data\csv\\sort\\" + kind + "\\ROE.csv", encoding='utf-8', mode='w', header=False)
# dataPBR.to_csv("E:\99.Coding\\18_D_Apple\Data\csv\\sort\\" + kind + "\\PBR.csv", encoding='utf-8', mode='w', header=False)
# dataEV.to_csv("E:\99.Coding\\18_D_Apple\Data\csv\\sort\\" + kind + "\\EV.csv", encoding='utf-8', mode='w', header=False)
# dataBPS.to_csv("E:\99.Coding\\18_D_Apple\Data\csv\\sort\\" + kind + "\\BPS.csv", encoding='utf-8', mode='w', header=False)

##데이터 시각화
df["CurrentPrice"].plot()
df.Volume.plot(secondary_y=True, style='g')
plt.show()

print(df['Volume'].idxmax())