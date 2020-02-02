import tweepy
import datetime
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
FILENAME= 'last_seenid.txt'

def retrieve_lastseen_id(filename): # get the lastseenid from the file
    with open(filename,'r') as f_read:
        lastseen_id = int(f_read.read().strip())
    return lastseen_id

def store_lastseen_id(lastseenid,filename): #store last tweet with its id in the txt file to read later
    with open(filename,'w') as f_write:
        f_write.write(str(lastseenid))
    return

def retweetleme(tw_id): #retweet the tweet with tw_id
	api.retweet(tw_id)

tweetler = api.user_timeline()


def my_tweets():
	print("This is your time line.")
	print("*" *10)
	for tweet in tweetler:
		print(tweet.text)
	print("*" *10)

lastseenid = retrieve_lastseen_id(FILENAME) 
date_time = datetime.datetime.now() #current time


def time_diff (date1,date2): # returns diff in current time (date2) and tweet time (date1) in mins
	diff = date2 - date1
	mins = diff.total_seconds() / 60 
	mins = int(mins)
	return mins

my_tweets()

def responde_to_tweet(yazi):
	mentions = api.mentions_timeline() #this returns a tweepy ResultSet class (its objects are iterable like list)

	

	for mention in reversed(mentions):  # because mentions returns in reversed order of tweets in time
		#print(str(mention.id) + '--' + mention.text)
			#and (time_diff(mention.created_at,date_time) < 60
		if yazi in mention.text  : #if it was tweeted in last hour
			nikname = mention.user.screen_name
			realName = mention.user.name
			#print("#hello world is found")
			remiander= time_diff(mention.created_at,date_time)
			remiander = str(remiander)
			print("Responding tw from " + remiander + " minutes ago " + ' from the user : ' + nikname )
			print("this was the tweet " + " - " + mention.text)
			print("**********")

			api.update_status('@' + mention.user.screen_name + " Hello baby.. " ,mention.id)
		
			# print("tweetin createdat funku " , type(mention.created_at)) 
		else :
			#print("There is no such tweet with " , test , " hashtag in " , x , " minutes" )
			pass
#minutee  = int(input("Check how old tweets ? ")) # to extent the code for getting tweets from spec time ago
#hashtg = input("Hashtag = ? ") # getting specific #hashtags in mentions

def get_other_user(uname):  # get some username as input and get all tweets

    list_of_user = api.user_timeline(uname, tweet_mode="extended")

    for tweex in list_of_user:

        if tweex.full_text[0:2] != "RT":
            print("*** " + tweex.full_text)

while True:
  responde_to_tweet("test")
	time.sleep(30)
