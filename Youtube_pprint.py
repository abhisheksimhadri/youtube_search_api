import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
 
# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/IN/most_popular?v=2&alt=jsonc")
r.text
 
# Convert it to a Python dictionary
data = json.loads(r.text)

pprint(data)
