#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
import csv
 
csvfile = 'csv1.csv'
f = open(csvfile, "r")
reader = csv.reader(f)
# header = next(reader)
 
for row in reader:
        print (row)
 
f.close()