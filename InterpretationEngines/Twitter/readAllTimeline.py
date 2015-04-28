import twitterAccess
import lastReadTweetData
import tweepy
#The whole point of this module is to get all the previously unread tweets
#and pass them back in some sort of format to whatever requests it.



#Returns a list of tweets
def pullAllNonReadTweetsFromUserTimeline():
    listofthings = []
    mylastread = lastReadTweetData.lastID()
    lastReadFlag = True
    for page in tweepy.Cursor(twitterAccess.api.user_timeline, since_id=mylastread).pages():
        for tweet in page:
            if lastReadFlag:
                lastReadTweetData.rewriteLastID(tweet.id)
                print("Rewrote last id as" + str(tweet.id))
                lastReadFlag = False
            listofthings.append(tweet)
            print("Appended Tweet")
        print("New Page")
    return listofthings

def pullAllNonReadTweetsFromListTimeline(mylistid):
    listofthings = []
    mylastread = lastReadTweetData.lastID()
    lastReadFlag = True
    for page in tweepy.Cursor(twitterAccess.api.list_timeline, owner='culturedcallie', list_id=mylistid, since_id=mylastread).pages():
        for tweet in page:
            if lastReadFlag:
                lastReadTweetData.rewriteLastID(tweet.id)
                print("Rewrote last id as" + str(tweet.id))
                lastReadFlag = False
            listofthings.append(tweet)
            print("Appended Tweet")
        print("New Page")
    return listofthings

#This should start this Timeline out at the very first tweet
def resetTimelineStartPoint():
    lastReadTweetData.resetIDtoStart()

def getAllListsIds():
    mylists = twitterAccess.api.lists_all()
    for l in mylists:
        print(l.slug)
        print(l.id)
