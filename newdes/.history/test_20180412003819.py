#coding:utf-8

import csv   #csvモジュールをインポートする

f = open('output.csv', 'rb')

dataReader = csv.reader(f)

for row in dataReader:
   print (row)