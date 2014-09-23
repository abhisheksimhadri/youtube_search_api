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
category = []
	

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
   try: category.append(item['category'])
   except KeyError: category.append(0)


#print views
#print likes
#print rating
#print category


views_people = []
views_film = []
views_entertainment = []
views_howto = []
views_tech = []
views_comedy = []
views_travel = []
views_music = []
category_anova = list(set(category))
print category_anova

for item in data['data']['items']:
	if (item['category'] == "People"):
		views_people.append(item['viewCount'])
	if (item['category'] == "Entertainment"):
		views_entertainment.append(item['viewCount'])
	if (item['category'] == "Film"):
		views_film.append(item['viewCount'])
	if (item['category'] == "Music"):
		views_music.append(item['viewCount'])
	if (item['category'] == "Travel"):
                views_travel.append(item['viewCount'])
        if (item['category'] == "Howto"):
                views_howto.append(item['viewCount'])
        if (item['category'] == "Tech"):
                views_tech.append(item['viewCount'])
        if (item['category'] == "Comedy"):
                views_comedy.append(item['viewCount'])


fig = plt.figure()
#ax = fig.add_subplot(views_people, views_entertainment, views_film, views_music, views_howto, views_tech, views_comedy, views_travel)
ax = fig.add_subplot(111)

(f_val, p_val) = stats.f_oneway(views_people, views_entertainment, views_film, views_music, views_howto, views_tech, views_comedy, views_travel)
print f_val, p_val
#two_sample_diff_var = stats.ttest_ind(x,y,equal_var=False)
#print "The t-statistic is %.3f and the p value is %.3f", % two_sample
#print "If we assume unequal variances then the t-statistic is %.3f and p value is %.3f" % two_sample_diff_var

ax.boxplot([views_people, views_entertainment, views_film, views_music, views_howto, views_tech, views_comedy, views_travel])
plt.show()

