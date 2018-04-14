# -*- coding: utf-8 -*-
import urllib
import sys
import io
import csv

# デフォルト文字コードをutf8に変更
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#各HTMLを構成するテキストを開く
f_html = open('index3.html','wb')
f_top = open('Text/head.txt','r',encoding="utf-8")
f_sectionstart = open('Text/section_start.txt','r',encoding="utf-8")
f_sectionend = open('Text/section_end.txt','r',encoding="utf-8")
f_end = open('Text/end.txt','r',encoding="utf-8")

#各HTMLを構成するテキストを読み込む
StringTop = f_top.read()
StringSectionStart = f_sectionstart.read()
StringSectionEnd = f_sectionend.read()
StringEnd = f_end.read()

#csvオープン・読み込み
argvs = sys.argv
csvfile = "./files/" + argvs[]
f = open(csvfile, "r")
reader = csv.reader(f)

TEXT = ""
for row in reader:
    print (row)
    TEXT = TEXT + StringSectionStart  + "<p>" + "</br>" + row[0] + row[1] + "</p>"
    if len(row) == 3:
        TEXT = TEXT + "<img class=\"img-fluid\" src=\"" + row[2] + "\" alt=\"\">"
    TEXT = TEXT + StringSectionEnd

#最終的なHTML文章の生成
HTML = StringTop + TEXT + StringEnd

#エラーを出す面倒な文字を除外
f_html.write(HTML.encode('cp932', 'ignore'))

# ファイルクローズ
f.close()
f_top.close()
f_sectionstart.close()
f_sectionend.close()
f_end.close()