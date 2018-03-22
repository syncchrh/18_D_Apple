# -*- coding:utf-8 -*-

import csv
import os


def setCsv(filename, data):
    with open(filename, 'a', encoding='UTF-8', newline="") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(data)

