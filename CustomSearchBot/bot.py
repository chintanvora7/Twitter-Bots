#Following is the Tweet Listener Module. It uses Twitter DM to recieves queries and send it to the Editorial logic script - search.py
#All Twitter API configurations are done here below so if the bot changes, please change the keys down below
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, json, search
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'p2nfNrvxlcfkTTnh3HbdpSoBz' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'm8SxwarZuiqU0yCAd3e9RY8AIDAzJaiaWSw03wm4PZjtPoH3dh'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3066074927-IWBSMe5NHeNxK09avcgtD8qjDX2tdWXeRTFaEjs'#keep the quotes, replace this with your access token
ACCESS_SECRET = '7o9NL6YxRc81y9tkoY6iM0EDt48M4A5ZhBToVvhDaA8la'#keep the quotes, replace this with your access token secret

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#client = wolframalpha.Client('H9AL7X-X4JERAYVE8')

#This destroys messages once we have emailed the user and we no longer require the message
def destroy_messages():
	messages = api.direct_messages()
	#print messages
	for i in range(len(messages)):
		each_id = messages[i].id
		api.destroy_direct_message(each_id)
		

#This gets as input an array of JSON objects of Tweets which will be parsed to get queries from each. These queries are then sent to the editorial logic module - search.py in this case. If it gets a valid result set, it will send out an email (mail.py) and destroy the message so the bot inbox is tidy and there are no duplicates
def queue(message_queue):
	for msg in message_queue:
		print msg.text, msg.created_at, msg.sender_id
		query = msg.text
		msg_id = msg.id
		sender_id = msg.sender_id
		result = search.set_query_from_tweet(query)	#calls search script and sends the Query
		m = ""
		if result == True:
			m = "Please Check configured email for the results"+" "+str(msg.created_at)
		else:
			m = "Something went wrong... Please Try again"+" "+str(msg.created_at)
		api.send_direct_message(user_id=sender_id,text=m)
		api.destroy_direct_message(msg_id)	
	

#Following is the main of the Bot.py script. Here, every 't' seconds, the bot checks it DM feed to see if there are any messages (in this case queries). If there are, it sends it to queue function
while True:
	t = 90
	message = api.direct_messages()
	if not message:
		print "no message recieved"
	else:
		try:
			queue(message)
		except Exception,e:
			print e
			destroy_messages()
			#api.destroy_direct_message(message[0].id)
	time.sleep(t)	




