import os
import sys
import weibo
import webbrowser
import json
 
APP_KEY = '3586469417'
MY_APP_SECRET = 'a5a5c8f8797979119e259d199012f046'
REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'
 
client = weibo.APIClient(APP_KEY, MY_APP_SECRET)
 
access_token = '2.00d_KLoDvW9iuD4f32be1132s9YmnC'
expires_in = 1527353899
 
client.set_access_token(access_token, expires_in)

print expires_in
client.statuses.update.post(status=u'hello, i mean no harm')
print "*************OK**********"

