### Stock Producer
* Create new topic named stockData
```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stockData
```
Should be three topics:
```
sud@sud-pc:~/kafka_2.11-0.10.0.0$ bin/kafka-topics.sh --list --zookeeper localhost:2181
stockData
stockTwitsStream
twitterStream
```
* Run submitjob.py:
```
python submitjob.py
```
It calls stockProducer.py  netfonds and fetches the stock data in the following format:
The stock data is fetched as follow:
```
time	            price	  quantity	source	buyer	seller	initiator
20161107T153000	  59.96	  58896	    Auto trade			
20161107T153000	  59.92	  300	      Auto trade			
20161107T153000	  59.93	  100	      Auto trade			
```

####
* Kill all python processes:
```
ps -ef | grep "python"
pkill -f python
```
