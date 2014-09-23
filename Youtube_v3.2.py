import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange, array, ones, linalg
from pylab import *
from scipy import stats

 
# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/TW/most_popular?v=2&alt=jsonc")
r.text
 
# Convert it to a Python dictionary
data = json.loads(r.text)

views = []
likes = []
rating = []
ratingcount = []
favorite = []
	

# Loop through the result.
for item in data['data']['items']:
 
   print "Video Title: %s" % (item['title'])
 
   print "Video Category: %s" % (item['category'])
 
   print "Video ID: %s" % (item['id'])
   
   if (isinstance(item['rating'], (int, long))):
      print "Video Rating: %f" % (item['rating'])
 
   print "Embed URL: %s" % (item['player']['default'])
 
   print "Views: %s" % (item['viewCount'])
   
   print "Likes: %s" % (item['likeCount'])

   print "Favorites: %s" % (item['favoriteCount'])

   print "Rating Count: %s" % (item['ratingCount'])

   print
   
   views.append(item['viewCount'])
   likes.append(float(item['likeCount']))
   rating.append(item['rating'])
   ratingcount.append(item['ratingCount'])
   favorite.append(item['favoriteCount'])


slope, intercept, r_value, p_value, std_err = stats.linregress(views, likes)
print " Y = %f * X + %f " % (slope, intercept)
print "R value", r_value
print "P Value", p_value
print "Standard Deviation", std_err


m,b = polyfit(views, likes, 1)
print(b)
print(m)
yp = polyval([m,b], views)
plot(views, yp)
scatter(views, likes)
grid(True)
xlabel('Views')
ylabel('Likes')
show()

