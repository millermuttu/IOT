import os
import time
import json
import urllib2
import os
import couchdb

def measure_temp():
	temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").readline()
	return (temp.replace("temp=",""))

while True:
	print(measure_temp())
	temp_now = measure_temp()
	data ={"temperature_of_pi":temp_now[:-1]}
	couch = couchdb.Server('http://admin:admin@127.0.0.1:5984/')
	db = couch['temp_rpi']
	db.save(data)
	with open('temp_data.json','w') as f:
		json.dump(data, f)

	time.sleep(10)

