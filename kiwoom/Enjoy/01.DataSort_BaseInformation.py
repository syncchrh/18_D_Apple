#-*- coding: utf-8 -*-
import csv
from pandas import Series, DataFrame
import numpy as np
import pandas as pd

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



df = pd.read_csv("E:\99.Coding\\18_D_Apple\Data\csv\\baseInformationKospi.csv", names=['code', 'name', 'volume', 'currentPrice', 'PER', 'EPS', 'ROE', 'PBR', 'EV', 'BPS', 'salesAccount', 'operatingProfit', 'perProfit', 'total'])

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
