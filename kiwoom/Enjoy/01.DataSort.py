import csv
from pandas import Series, DataFrame
import numpy as np


test = []
filename = "E:\99.Coding\\18_D_Apple\Data\csv\\baseInformationKospi.csv"
with open(filename, 'r', newline='', encoding='UTF-8') as f:
    csvReader = csv.reader(f)
    for row in csvReader :
        test.append(row)
        #print(row)


print(test)


#numpy array 로 변환
#arr = np.array(test)


# #Transpose
# arrT = arr.T
#
# #print(arr.shape)
# #print(arr)
# #print(arrT)
#
#
# raw_data = {'date' : arrT[0],
#             'present' : arrT[1],
#             'open': arrT[2],
#             'high': arrT[3],
#             'low': arrT[4],
#             'volume': arrT[5],
#             'tradingValue': arrT[6]}
#
# #print(raw_data)
#
# #Pandas 자료형으로 변환
# data = DataFrame(raw_data, columns=['present', 'open', 'high', 'low', 'volume', 'tradingValue'], index=arrT[0])
# #data = DataFrame(raw_data)
#
# print(data.ix['20180319'])
#
# #np.save('test',data)
# print(data)


