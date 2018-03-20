import csv
import os


def setCsv(filename, data):
    f = open(filename, 'w')
    csvWriter = csv.writer(f)

    csvWriter.writerow(data)
    f.close()

