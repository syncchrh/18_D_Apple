import csv
from pandas import Series, DataFrame
import numpy as np
from Module_Sseung import CSVFileIO


test = []
shcode = []

#[0]:현재가, [1]:거래량, [2]:거래대금 , [3]:일자, [4]:시가, [5]:고가,      [6]:저가
#[0]:일자,   [1]:현재가, [2]:시가,      [3]:고가, [4]:저가  [5]:거래량 ,   [6]:거래대금
filename = "/home/sseung/01.Coding/18_D_Apple/Data/csv/output.csv"
with open(filename, 'r', newline='', encoding='UTF-8') as f:
    csvReader = csv.reader(f)
    for row in csvReader :
        test.append(row[0:7])

filename = "/home/sseung/01.Coding/18_D_Apple/Data/csv/shcode.csv"
with open(filename, 'r', newline='', encoding='UTF-8') as f:
   csvReader = csv.reader(f)
   for row in csvReader:
       shcode.append(row)


#numpy array 로 변환
arr = np.array(test)
arrT = arr.T


raw_data = {'present' : arrT[0],
            'volume' : arrT[1],
            'tradingValue': arrT[2],
            'date': arrT[3],
            'open': arrT[4],
            'high': arrT[5],
            'low': arrT[6]}

#print(raw_data)

#Pandas 자료형으로 변환
data = DataFrame(raw_data, columns=['open', 'high', 'low', 'volume', 'tradingValue', 'present'], index=arrT[3])
#data = DataFrame(raw_data, columns=['open', 'high', 'low', 'volume', 'tradingValue', 'present'], index=arrT[4])

#Pandas 데이터 저장
data.to_csv("/home/sseung/01.Coding/18_D_Apple/Data/csv/output_017800.csv", encoding='utf-8', mode='a', header=False)

#Pandas 데이터 불러오기
#data.from_csv("E:\99.Coding\\18_D_Apple\Data\csv\\output_017800.csv")


