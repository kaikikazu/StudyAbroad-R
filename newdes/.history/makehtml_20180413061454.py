# -*- coding: utf-8 -*-
import json
import requests
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

TEXT = ""
#HTMLを生成する
for tweet in data:
    tweetlist = []
    print(tweet["text"])
    date = tweet["created_at"].split() #日時
    DATE = makedate(date)
    tweetlist.append(DATE)
    index = tweet["text"].find("https://t.co") #元ツイートが簡単に辿れるURL
    #ツイートを取得、HTMLの文章を生成
    if index != -1:
        TEXT = TEXT + StringSectionStart + "<p>" + "</br>" + DATE + tweet["text"][0:index] + "</p>"
        tweetlist.append(tweet["text"][0:index])
    else:
        TEXT = TEXT + StringSectionStart + "<p>" + "</br>" + DATE + tweet["text"] + "</p>"
        tweetlist.append(tweet["text"])
    #もし、画像付きツイートだった場合、画像を取得してHTMLに埋め込み
    if len(tweet["entities"]) == 5:
        print(tweet["entities"]["media"][0]["media_url"])
        TEXT = TEXT + "<img class=\"img-fluid\" src=\"" + tweet["entities"]["media"][0]["media_url"] + "\" alt=\"\">"
        tweetlist.append(tweet["entities"]["media"][0]["media_url"])
    TEXT = TEXT + StringSectionEnd
    print(tweetlist)
    writer.writerow(tweetlist)
    csvlist.append(tweetlist)

#最終的なHTML文章の生成
HTML = StringTop + TEXT + StringEnd

#エラーを出す面倒な文字を除外
f_html.write(HTML.encode('cp932', 'ignore'))

# csvファイルに出力
#writer.writerow(csvlist)

# ファイルクローズ
f.close()
f_top.close()
f_sectionstart.close()
f_sectionend.close()
f_end.close()