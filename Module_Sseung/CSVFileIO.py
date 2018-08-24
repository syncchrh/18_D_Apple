# -*- coding:utf-8 -*-

import csv
import os


def setCsv(filename, data):
    f = open(filename, 'a', encoding='UTF-8', newline="")
    csvWriter = csv.writer(f)
    csvWriter.writerow(data)
   # f.close()

