#!/usr/bin/python
# coding: UTF-8
 
f = open('pass/Keys.txt')
lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ

print (lines2[0])