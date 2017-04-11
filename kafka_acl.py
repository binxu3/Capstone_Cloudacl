# kafka_acl

from kafka import KafkaProducer
from kafka.errors import KafkaError,KafkaTimeoutError

import argparse
import json
import re
import time
import schedule
import os
import logging
import atexit
import requests

topic_name='log-analyzer'
filepath='/Users/binxu/Documents/tigercode/Capstone_Cloudacl/2017-03-05/acl_100.txt'


logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('acl')
logger.setLevel(logging.DEBUG)

def ipdecoder(ip):
    freegeoip = 'http://freegeoip.net/json/'
    url=freegeoip+ip
    response=requests.get(url)
    
    
    return response.json()


if __name__ =='__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument('topic_name',help='the kafka topic push to')
	parser.add_argument('kafka_broker',help='the location of the kafka broker')

	args=parser.parse_args()
	topic_name = args.topic_name
	kafka_broker = args.kafka_broker

	producer = KafkaProducer(bootstrap_servers=kafka_broker)
	with open(filepath,'r') as f:
		for line in f:
			tmp=line.encode('utf-8').strip()
			m=re.match(r'(?P<ip>.*?) .*?\[(?P<date>.*?)\].*[&\?]ur[li]=(?P<url>.*?)&cat=(?P<category>.*?)[ &].*', tmp)
			if m != None:
				ip,date,url,cat=m.groups()
				location=ipdecoder(ip)
				city=location['city']
    			country=location['country_name']
    			state=location['region_code']
			#data = ('country:{},state:{},date:{},url:{},cat:{}'.format(country,state,date,url,cat))
			data = json.dumps(
				{
				'country': country,
				'state':state,
				'date':date,
				'url':url,
				'cat':cat
				}
				)
			producer.send(topic=topic_name,value=data,timestamp_ms=time.time())
	logger.debug('Send log data into %s',topic_name)
