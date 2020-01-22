# hungryclient test
# this client send dozens of requests every second


from __future__ import division
from time import sleep
import httplib2
import json


h = httplib2.Http()

# Set url to attack
url = 'http://api.github.com'

# Set number of request to send per minute
req_per_minute = 20000

# calucul number of request per second
interval = (60.0 / req_per_minute)

def SendRequests(url, req_per_minute):
	requests = 0 
	while requests < req_per_minute:
		result = json.loads(h.request(url,'GET')[1])
		if result.get('error') is not None:
			print ("Error #%s : %s" %(result.get('error'), result.get('data')))
			print ("Hit rate limit. Waiting 5 seconds and trying again...")
			sleep(5)
			SendRequests(url, req_per_minute)
		else:
			print  ("Number of Requests: ", requests+1)
			print (result.get('response'))
		requests = requests + 1 
		sleep(interval)

print ("Sending Requests...")
SendRequests(url, req_per_minute)