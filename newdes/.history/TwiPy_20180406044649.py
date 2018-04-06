# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session, OAuth1
import json
import requests
import urllib
import sys
import io

#検索文字列設定
word = urllib.parse.quote_plus("#桜 exclude:retweets")

# デフォルト文字コードをutf8に変更
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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
f_top = open('Text/head.txt','r',encoding="shift_jis")
f_sectionstart = open('Text/section_start.txt','r',encoding="shift_jis")
f_sectionend = open('Text/section_end.txt','r',encoding="shift_jis")
f_end = open('Text/end.txt','r',encoding="shift_jis")

StringTop = f_top.read()
StringSectionStart = f_sectionstart.read()
StringSectionEnd = f_sectionend.read()
StringEnd = f_end.read()

TEXT = ""

#HTMLを生成する
for tweet in data:
    print(tweet["text"])
    #ツイートを取得、HTMLの文章を生成
    TEXT = TEXT + StringSectionStart + "<p>" + "</br>" + tweet["text"] + "</p>"
    #もし、画像付きツイートだった場合、画像を取得してHTMLに埋め込み
    if len(tweet["entities"]) == 5:
        print(tweet["entities"]["media"][0]["media_url"])
        TEXT = TEXT + "<img class=\"img-fluid\" src=\"" + tweet["entities"]["media"][0]["media_url"] + "\" alt=\"\">"
    TEXT = TEXT + StringSectionEnd

HTML = StringTop + TEXT + StringEnd
#面倒な文字を除外
f_html.write(HTML.encode('cp932', 'ignore'))

f_top.close()
f_sectionstart.close()
f_sectionend.close()
f_end.close()