# -*- coding: utf-8 -*-

from kafka import *
from cashtag import cashtag
from twython import TwythonStreamer
import pprint
import re
import json
from cashtagSet import cashtagSet


# kafka setup

mykafka = KafkaClient("localhost:9092")
producer = SimpleProducer(mykafka)
topicName = "twitterStream"


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data
            producer.send_messages(topicName, json.dumps(data))
    def on_error(self, status_code, data):
    	print '!!! error occurred !!!'
    	print self
    	print data
        print status_code


CONSUMERKEY = "NJDw5JVBjjjUiiqcxtxwnBzq1"
CONSUMERSECRET = "hBX9liZV0q5DKKIsKrCcfXg5toe3CBbZmWA6cEp9bWh9rWljna"
OAUTHTOKEN = "102364682-rjjnlF4WvdblszBYm47wexCtM3iJMUgefK2pf5AA"
OAUTHTOKENSECRET="U93jNaO0EKTUJdWc92BOggPG2KfHSDfY40CM0mgWIYnob"

try:
    stream = MyStreamer(CONSUMERKEY, CONSUMERSECRET, OAUTHTOKEN, OAUTHTOKENSECRET)
    #twitterFilter = cashtag('NYSE100')+cashtag('NASDAQ100')+cashtag('DOW30')+cashtag('COMPANIES')+cashtag('SP500')
    twitterFilterSet = cashtagSet('NYSE100')+cashtagSet('NASDAQ100')+cashtagSet('DOW30')+cashtagSet('COMPANIES')+cashtagSet('SP500')
    print(len(twitterFilterSet.split(',')))
    #print(twitterFilter.split(','))

    results = stream.statuses.filter(track=twitterFilterSet)

    #print(results)

except Exception, e:
	print(e)