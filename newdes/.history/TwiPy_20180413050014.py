# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session, OAuth1
import json
import requests
import urllib
import sys
import io
import csv

#検索文字列設定
word = urllib.parse.quote_plus("#留学クリコアラ exclude:retweets")

# デフォルト文字コードをutf8に変更
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ファイルオープン
f = open('output.csv', 'w',errors='ignore')
writer = csv.writer(f, lineterminator='\n')

#twitterAPIのkeyを読み込む
f = open('../pass/Keys.txt')
keys = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()

#apiキー情報設定
consumer_key = keys[0].replace('\n','')
consumer_key_secret = keys[1].replace('\n','')
access_token = keys[2].replace('\n','') 
access_token_secret = keys[3].replace('\n','')

#twitterAPIアクセス
url = "https://api.twitter.com/1.1/search/tweets.json?count=15&lang=ja&q=" + word
auth = OAuth1(consumer_key, consumer_key_secret, access_token, access_token_secret)
response = requests.get(url, auth = auth)
data = response.json()['statuses']

#各HTMLを構成するテキストを読み込む
f_html = open('index2.html','wb')
f_top = open('Text/head.txt','r',encoding="utf-8")
f_sectionstart = open('Text/section_start.txt','r',encoding="utf-8")
f_sectionend = open('Text/section_end.txt','r',encoding="utf-8")
f_end = open('Text/end.txt','r',encoding="utf-8")

StringTop = f_top.read()
StringSectionStart = f_sectionstart.read()
StringSectionEnd = f_sectionend.read()
StringEnd = f_end.read()

TEXT = ""

def makedate(date):
    dateText = ""
    if date[1] == "Jan":
        dateText = "1"
    elif date[1] == "Feb":
        dateText = "2"
    elif date[1] == "Mar":
        dateText = "3"
    elif date[1] == "Apr":
        dateText = "4"
    elif date[1] == "May":
        dateText = "5"
    elif date[1] == "Jun":
        dateText = "6"
    elif date[1] == "Jul":
        dateText = "7"
    elif date[1] == "Aug":
        dateText = "8"
    elif date[1] == "Sep":
        dateText = "9"
    elif date[1] == "Oct":
        dateText = "10"
    elif date[1] == "Nov":
        dateText = "11"
    elif date[1] == "Dec":
        dateText = "12"
    dateText = dateText + "/" + date[2] + " "
    return dateText

# データを保存するリスト
csvlist = []

#HTMLを生成する
for tweet in data:
    tweetlist = []
    print(tweet["text"])
    date = tweet["created_at"].split() #日時
    DATE = makedate(date)
    index = tweet["text"].find("https://t.co")
    #ツイートを取得、HTMLの文章を生成
    #元ツイートが簡単に辿れるURLが付属してしまうので削除
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
    csvlist.append(tweetlist)

HTML = StringTop + TEXT + StringEnd
#面倒な文字を除外
f_html.write(HTML.encode('cp932', 'ignore'))

# 出力
writer.writerow(csvlist)

# ファイルクローズ
f.close()

f_top.close()
f_sectionstart.close()
f_sectionend.close()
f_end.close()