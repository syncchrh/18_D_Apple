import csv



test = []
test2 = []

#[0]:현재가, [1]:거래량, [2]:거래대금 , [3]:일자, [4]:시가, [5]:고가,      [6]:저가
#[0]:일자,   [1]:현재가, [2]:시가,      [3]:고가, [4]:저가  [5]:거래량 ,   [6]:거래대금
filename = "E:\99.Coding\\18_D_Apple\Data\output.csv"
with open(filename, 'r', newline='', encoding='UTF-8') as f:
    csvReader = csv.reader(f)
    for row in csvReader :
        test.append(row[0:7])
        test2.append(row[0:7])

for i in range(0,300) :
    test[i][0] = test2[i][3]
    test[i][3] = test2[i][0]
    test[i][1:2] = test[i][3:7]
    test[i][5:6] = test2[i][1:3]
    test[i] = test[i][0:7]

print(test[0])


