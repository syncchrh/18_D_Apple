import csv



test = []

def getCsv(filename):
    f = open(filename, 'r', encoding='utf-16')
    csvReader = csv.reader(f)
    for row in csvReader:
        test.append(row)

    return csvReader

getCsv("E:\99.Coding\\18_D_Apple\Data\output.csv")
print(test[1])