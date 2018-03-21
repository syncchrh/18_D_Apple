import csv
import os


def setCsv(filename, data):
    f = open(filename, 'w', encoding='utf-16')
    csvWriter = csv.writer(f)

    csvWriter.writerow(data)
    f.close()


