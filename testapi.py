import os
import sys
import weibo
import webbrowser
import json
 
APP_KEY = '3586469417'
MY_APP_SECRET = 'a5a5c8f8797979119e259d199012f046'
REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'
 
client = weibo.APIClient(APP_KEY, MY_APP_SECRET)
 
authorize_url = client.get_authorize_url(REDIRECT_URL)

webbrowser.open(authorize_url)
 
code = raw_input("input the code: ").strip()
 
request = client.request_access_token(code, REDIRECT_URL)
 
access_token = request.access_token
expires_in = request.expires_in
uid = request.uid
 
client.set_access_token(access_token, expires_in)

client.statuses.update.post(status=u'I am a robot, put up your hands!')
print "*************OK**********"

