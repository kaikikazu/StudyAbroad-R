# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session, OAuth1
import json
import requests
import urllib
import sys
import io

#検索文字列設定
word = urllib.parse.quote_plus("#留学")

# デフォルト文字コードをutf8に変更
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#apiキー情報設定
consumer_key = "mn7MQJ8YbDCNv16VnRVG9MTYW"
consumer_key_secret = "p6XHIdla4KJnza7IyIGqcCcCpN3FJJzJkR1Wx3clbpl0kChyhE"
access_token = "2534309018-Ekv63oCR81e4H06vnw1aQImPAXEVTyt94ir9gQF"
access_token_secret = "DhxuLe6NtKB9gqg32Eo0rGWpDrv8sLkSCPGY2SJOHaLxZ"

#twitterAPIアクセス
url = "https://api.twitter.com/1.1/search/tweets.json?count=100&lang=ja&q=" + word
auth = OAuth1(consumer_key, consumer_key_secret, access_token, access_token_secret)
response = requests.get(url, auth = auth)
data = response.json()['statuses']

f_top = open('PageText/top.txt','r',encoding="utf-8_sig")
f_text = open('HTML/index.html','wb')
f_TextToImage = open('PageText/TextToImage.txt','r')
f_image = open('PageText/image.txt','w')
f_end = open('PageText/end.txt','r',encoding="utf-8_sig")

TEXT = ""
IMAGE = ""
StringTop = f_top.read()
StringTextToImage = f_TextToImage.read()
StringEnd = f_end.read()

#データ表示
for tweet in data:
    print(tweet["text"])
    TEXT = TEXT + tweet["text"] + "</br></br>"
    if len(tweet["entities"]) == 5:
    	print(tweet["entities"]["media"][0]["media_url"])
    	IMAGE = IMAGE + "<li><img src=\"" + tweet["entities"]["media"][0]["media_url"] + "\" width=\"360\" height=\"350\" alt=\"\"></li>"

HTML = StringTop + TEXT + StringTextToImage + IMAGE + StringEnd
f_text.write(HTML.encode('cp932', 'ignore'))

f_text.close()
f_TextToImage.close()
f_image.close()
f_end.close()