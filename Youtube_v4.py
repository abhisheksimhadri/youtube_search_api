import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange, array, ones, linalg
from pylab import *
from scipy import stats

 
# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/IN/most_popular?v=2&alt=jsonc")
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
   
   try: print "Video Rating: %f" % (item['rating'])
   except KeyError: pass
 
   print "Embed URL: %s" % (item['player']['default'])
 
   try: print "Views: %s" % (item['viewCount'])
   except KeyError: pass

   try: print "Likes: %s" % (item['likeCount'])
   except KeyError: pass

   print "Favorites: %s" % (item['favoriteCount'])

   try: print "Rating Count: %s" % (item['ratingCount'])
   except KeyError: pass

   print
   
   try: views.append(item['viewCount'])
   except KeyError: views.append(0)
   try: likes.append(float(item['likeCount']))
   except KeyError: likes.append(0)
   try: rating.append(item['rating'])
   except KeyError: rating.append(0)
   try: ratingcount.append(item['ratingCount'])
   except KeyError: ratingcount.append(0)
   try: favorite.append(item['favoriteCount'])
   except KeyError: favorite.append(0)

#missing_views = np.isnan(views)
#missing_rating = np.isnan(rating)
#views_new = views[~missing_views]
#rating_new = rating[~missing_rating]
#views.fillna(0)

#views_new = FixNaNs(views)
#rating_new = FixNaNs(rating)

#print views
#print rating


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

