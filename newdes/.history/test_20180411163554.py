# -*- coding: utf-8 -*-

import csv

# ファイルオープン
f = open('output.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

# データをリストに保持
csvlist = []
csvlist.append("hoge")
csvlist.append("fuga")

# 出力
writer.writerow(csvlist)

# ファイルクローズ
f.close()