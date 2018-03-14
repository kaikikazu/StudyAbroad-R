CONSUMER_KEY        = 'mn7MQJ8YbDCNv16VnRVG9MTYW'
CONSUMER_SECRET_KEY = 'p6XHIdla4KJnza7IyIGqcCcCpN3FJJzJkR1Wx3clbpl0kChyhE'
ACCESS_TOKEN        = '2534309018-Ekv63oCR81e4H06vnw1aQImPAXEVTyt94ir9gQF'
ACCESS_TOKEN_SECRET = 'DhxuLe6NtKB9gqg32Eo0rGWpDrv8sLkSCPGY2SJOHaLxZ'

import json
from twitter import *

f = open('test.txt','w')

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))

#timelines = t.statuses.home_timeline()
f = open('test.txt','w')

#for timeline in timelines:
    #tl = ' [{username}]:{text}'.format(
            #username=timeline['user']['name'], text=timeline['text'])
    #print (tl + "</br>")

searchTweets = t.search.tweets(q = "Qiita")

for searchTweets in searchTweets:
    sr = searchTweets['name']
    print (sr + "</br>")