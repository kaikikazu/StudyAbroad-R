import csv

f = open('output.csv', 'r')

reader = csv.reader(f)
header = next(reader)
for row in reader:
    print (row)

f.close()