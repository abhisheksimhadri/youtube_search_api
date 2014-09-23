import gdata.docs.service

# Create a client class which will make HTTP requests with Google Docs server.
client = gdata.docs.service.DocsService()
# Authenticate using your Google Docs email address and password.
client.ClientLogin('abhisheksimhadri@gmail.com', 'aumsairam')

# Query the server for an Atom feed containing a list of your documents.
documents_feed = client.GetDocumentListFeed()
# Loop through the feed and extract each document entry.
for document_entry in documents_feed.entry:
  # Display the title of the document on the command line.
  print document_entry.title.text

import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

# Turn on HTTPS/SSL access.
# Note: SSL is not available at this time for uploads.
yt_service.ssl = True

def GetAuthSubUrl():
  next = 'http://www.example.com/video_upload.pyc'
  scope = 'http://gdata.youtube.com'
  secure = False
  session = True

yt_service = gdata.youtube.service.YouTubeService()
return yt_service.GenerateAuthSubURL(next, scope, secure, session)

authSubUrl = GetAuthSubUrl()
print '<a href="%s">Login to your Google account</a>' % authSubUrl

#next — the URL of the page that YouTube should redirect the user to after they have authorized your application to access their account.
#scope — indicating that the application will only access YouTube API feeds.
#secure — indicating that the token returned will not be a secure token.
#session — indicating this token can be exchanged for a multi-use (session) token.

#Upgrading to a session token

import cgi
parameters = cgi.FieldStorage()
authsub_token = parameters[[]'token' ]

yt_service = gdata.youtube.service.YouTubeService()
yt_service.SetAuthSubToken(authsub_token)
yt_service.UpgradeToSessionToken()


