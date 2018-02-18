import tweepy
from textblob import TextBlob


consumer_key= '9688oZJkQrmcvn3ZDk49kXmP0'
consumer_secret='FSqJnhdHldKzOI76Q5SNK2Ktj2iAZeQWbHdAI4r2LUUXuIARXc'

access_token= '755309857880743936-XnHNjLjWeZCve28o0BfAwJpPLznbFoZ'
access_token_secret= 'QyXDp4Rku1LygFRrHvy6WRUWOr3jq4qGPSFKQf8akZEhk'

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#PriyaVarrier')

countp=0
countn=0
countnn=0

for tweets in public_tweets:
	print(tweets.text)
	analysis = TextBlob(tweets.text)
	if analysis.sentiment.polarity > 0:
            print('\tPOSITIVE\n')
            countp+=1
        elif analysis.sentiment.polarity == 0:
            print('\tNEUTRAL\n')
            countn+=1
        else:
            print('\tNEGATIVE\n')
            countnn+=1

print'total positive tweets percent:', (countp/15.0)*100
print'total negative tweets:',(countn/15.0)*100
print'total neutral tweets:',(countnn/15.0)*100

