import gdata.youtube
import gdata.youtube.service
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange, array, ones, linalg
from pylab import *
from scipy import stats
from scipy.io import loadmat


yt_service = gdata.youtube.service.YouTubeService()

yt_service.ssl = True

# A complete client login request & authentication
yt_service.email = ''
yt_service.password = ''
yt_service.source = ''
yt_service.developer_key = ''
yt_service.ProgrammaticLogin()

#storing data in arrays
title = []
category = []
duration = []
view = []
rating = []

#category details
views_Comedy = []
views_Entertainment = []
views_People = []
views_Autos = []
views_News = []
views_Music = []
views_Education = []
views_Howto = []
views_Nonprofit = []
views_Film = []
views_Games = []
views_Tech = []
views_Sports = []
views_Shows = []


#Displaying a video feed
#A soecific video entry can be entered using a Video ID - http://gdata.youtube.com/feeds/api/videos/videoID
def GetAndPrintVideoFeed(uri):
  yt_service = gdata.youtube.service.YouTubeService()
  feed = yt_service.GetYouTubeVideoFeed(uri)
  for entry in feed.entry:
    PrintEntryDetails(entry) 

#Displaying video entry contents
def PrintEntryDetails(entry):
  print 'Video title: %s' % entry.media.title.text
  title.append(entry.media.title.text)
  print 'Video published on: %s ' % entry.published.text
  #print 'Video description: %s' % entry.media.description.text
  print 'Video category: %s' % entry.media.category[0].text
  category.append(entry.media.category[0].text)
  if entry.media.category[0].text == "Comedy": views_Comedy.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Entertainment": views_Entertainment.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "People": views_People.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Autos": views_Autos.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "News": views_News.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Music": views_Music.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Education": views_Education.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Howto": views_Howto.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Nonprofit": views_Nonprofit.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Film": views_Film.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Games": views_Games.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Tech": views_Tech.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Sports": views_Sports.append(float(entry.statistics.view_count))
  if entry.media.category[0].text == "Shows": views_Shows.append(float(entry.statistics.view_count))
  #print 'Video tags: %s' % entry.media.keywords.text
  #print 'Video watch page: %s' % entry.media.player.url
  #print 'Video flash player URL: %s' % entry.GetSwfUrl()
  print 'Video duration: %s' % entry.media.duration.seconds
  duration.append(float(entry.media.duration.seconds))

  # non entry.media attributes
  if entry.geo: print "Video geo location: '{0}'" .format(entry.geo.location())
  #if entry.geo: print 'Video geo location: %s' % entry.geo.location()
  print 'Video view count: %s' % entry.statistics.view_count
  view.append(float(entry.statistics.view_count))
  if entry.rating: print 'Video rating: %s' % entry.rating.average
  if entry.rating: rating.append(float(entry.rating.average))

"""
  # show alternate formats
  for alternate_format in entry.media.content:
    if 'isDefault' not in alternate_format.extension_attributes:
      print 'Alternate format: %s | url: %s ' % (alternate_format.type, alternate_format.url)

  # show thumbnails
  for thumbnail in entry.media.thumbnail:
    print 'Thumbnail url: %s' % thumbnail.url

"""

#Retrieving standard feeds
def PrintVideoFeed(feed):
  i = 1
  for entry in feed.entry:
    print i
    i = i + 1
    PrintEntryDetails(entry)

#Retrieving standard feeds
def GetAndPrintFeedByUrl(feed):
  yt_service = gdata.youtube.service.YouTubeService()

  # You can retrieve a YouTubeVideoFeed by passing in the URI
  #uri = 'http://gdata.youtube.com/feeds/api/standardfeeds/JP/most_popular'
  PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))


#Retrieving videos uploaded by a specific user
def GetAndPrintUserUploads(username):
  yt_service = gdata.youtube.service.YouTubeService()
  uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads' % username
  PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))
  
#Retrieving related videos
#related_feed = yt_service.GetYouTubeRelatedVideoFeed(video_id='abc123')

#searching for videos
def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'viewCount'
  query.racy = 'exclude'
  query.max_results = 50
  query.start_index = 1
  query.time = 'this_month'
  feed = yt_service.YouTubeQuery(query)
  PrintVideoFeed(feed)

"""
Parameters:- 
author
Sets the author of the entry. Author is synonymous with YouTube username.
format
Specifies a video format. Accepts numeric parameters to specify one of two kinds of RTSP streaming URLs for mobile video playback or a HTTP URL to the embeddable Flash player.
racy
Indicates whether restricted content should be included in the results. Accepts only two parameters: 'include' or 'exclude'.
max_results
Sets the maximum number of entries to return at one time.
start_index
Sets the 1-based index of the first result to be retrieved (for paging).
orderby
Sets the order in which to list entries, such as by relevance, viewCount, published, or rating.
time
Sets a time period to limit standard feed results to: today, this_week, this_month, or all_time.
vq
Sets a search query term. Searches for the specified string in all video metadata, such as titles, tags, and descriptions.
"""

#searching for videos with categories and keywords
def SearchAndPrintVideosByKeywords(list_of_search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.orderby = 'viewCount'
  query.racy = 'exclude'
  for search_term in list_of_search_terms:
    new_term = search_term.lower()
    query.categories.append('/%s' % new_term)
  feed = yt_service.YouTubeQuery(query)
  PrintVideoFeed(feed)

"""
Searching by developer tags:-
developer_tag_uri = 'http://gdata.youtube.com/feeds/videos/-/%7Bhttp%3A%2F%2Fgdata.youtube.com%2Fschemas%2F2007%2Fdevelopertags.cat%7Dyour_tag_here'
yt_service = gdata.youtube.service.YouTubeService()
PrintVideoFeed(yt_service.GetYouTubeVideoFeed(developer_tag_uri))
"""

#uri = 'http://gdata.youtube.com/feeds/api/standardfeeds/most_popular'
#print GetAndPrintFeedByUrl(uri)  
  
search = 'social experiment'
print SearchAndPrint(search)


#Regression views with duration
slope, intercept, r_value, p_value, std_err = stats.linregress(view, duration)
print " Y = %f * X + %f " % (slope, intercept)
print "R value", r_value
print "P Value", p_value
print "Standard Deviation", std_err

m,b = polyfit(view, duration, 1)
print(b)
print(m)
yp = polyval([m,b], view)
plot(view, yp)
scatter(view, duration)
grid(True)
xlabel('Views')
ylabel('Duration')
show()

#Regression views with rating
slope, intercept, r_value, p_value, std_err = stats.linregress(view, rating)
print " Y = %f * X + %f " % (slope, intercept)
print "R value", r_value
print "P Value", p_value
print "Standard Deviation", std_err

m,b = polyfit(view, rating, 1)
print(b)
print(m)
yp = polyval([m,b], view)
plot(view, yp)
scatter(view, rating)
grid(True)
xlabel('Views')
ylabel('Rating')
show()

#Anova of category with Views
category_anova = list(set(category))
print category_anova

fig = plt.figure()
ax = fig.add_subplot(111)
(f_val, p_val) = stats.f_oneway(views_People, views_Entertainment, views_Sports, views_Comedy, views_Film, views_Shows)
ax.boxplot([views_People, views_Entertainment, views_Sports, views_Comedy, views_Film, views_Shows])
print f_val, p_val
ax.set_xticklabels(['People', 'Entertainment', 'Sports', 'Comedy', 'Film', 'Shows'])
#ax.set_yticklabels('Views')
plt.show()

"""
data_to_plot = [views_Comedy, views_Entertainment, views_People, views_Autos]
figure(1)
boxplot(data_to_plot)
labels = ('People', 'Autos', 'Comedy', 'Entertainment')
xticks(range(1,13),labels, rotation=15)
xlabel('Categories')
ylabel('Number')
title('Viral videos by Category')
"""

"""
fig = plt.figure()
ax = fig.add_subplot(111)
(f_val, p_val) = stats.f_oneway(views_Comedy, views_Entertainment, views_People, views_Autos, views_News, views_Music, views_Education, views_Howto, views_Nonprofit, views_Film)
print f_val, p_val
ax.boxplot([views_Comedy, views_Entertainment, views_People, views_Autos, views_News, views_Music, views_Education, views_Howto, views_Nonprofit, views_Film])
plt.show()
"""
