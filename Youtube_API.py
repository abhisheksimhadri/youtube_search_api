import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange, array, ones, linalg
from pylab import *

 
# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
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


#print favorite
#print
#print rating
#print
#print ratingcount
#print
#print views
#print
print likes
#print


#fig = plt.figure()

#ax = fig.add_subplot(121)
#ax.scatter(rating, views, color='blue', s=5, edgecolor= 'none')
#ax.set_aspect(1./ax.get_data_ratio())

#props = dict(alpha=0.5, edgecolors='none' )

#handles = []
#colors = ['blue', 'green', 'magenta', 'cyan']

#plt.show()

m,b = polyfit(likes, rating, 1)
print(b)
print(m)
yp = polyval([m,b], likes)
plot(likes, yp)
scatter(likes, rating)
grid(True)
xlabel('Likes')
ylabel('Rating')
show()

