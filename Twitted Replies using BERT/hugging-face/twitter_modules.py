import tweepy

# Keys, Tokens and Global Variables
CONSUMER_KEY='dOTh7F9TagnPJrv4cTqkQBnGQ' #Put API KEy
CONSUMER_SECRET='gqW2tRNwQFrhPzA1n8QcePxiXBVu8KdBttUkgFgYI44O3kruxy' #Put API Secret
ACCESS_KEY='1516075211183038468-Q614dLbfwHMAQUay9SZCp6LvgnDzJ7' #put Access key
ACCESS_SECRET='b0PQ4aEGYrtSUTKAbUjJ0HJqezzqaHMNXZoBQKvDSqdq2'  #Put Access Secret
lastMention=''
api=None

# Initialize API
def init_tweepy():
    global api
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)


# Check if there are any new queries
def checkmentions():
  global lastMention
  mentions = api.mentions_timeline()
  if len(mentions) == 0 :
      return None
  most_recent_mention = mentions[0]
  user = most_recent_mention.user.screen_name
  if lastMention==user:
    # No recent Tweets
    return None
  else:
    lastMention=user
    return most_recent_mention
    
    
# Tweet reponse to the customer
def tweet_to_customer(tweet_text, mention):
    user = mention.user.screen_name
    tweet_id = mention.id
    tweet = api.update_status('@'+user+' '+tweet_text,in_reply_to_status_id=tweet_id)
    
def retrieve_tweets_since(id):
	recent_tweets = api.mentions_timeline(since_ids=id)
	return recent_tweets
	
def get_last_tweetid_file():
    #Time stamp of latest Tweet
    f = open("lastTweet.txt","r")
    lastTweet_id = int(f.readline())
    f.close()
    return lastTweet_id
    
def update_last_tweetid_file(lastTweet_id):
    #Update Time stamp of latest Tweet
    f = open("lastTweet.txt","w")
    f.write(str(lastTweet_id))
    f.close()