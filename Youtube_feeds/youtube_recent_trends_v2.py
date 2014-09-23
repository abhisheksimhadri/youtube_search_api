import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
 
# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/most_recent?alt=json")
r.text
 
# Convert it to a Python dictionary
data = json.loads(r.text)
	
#print json.dumps(data, indent = 4)

for item in data['feed']['entry']:
	print "Video Title %s " %item['title']
	print "Video Category %s " %item['media$group']['media$category']
	print "Video Length %s " %item['media$group']['yt$duration']









