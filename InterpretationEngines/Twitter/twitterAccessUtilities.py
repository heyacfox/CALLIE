import twitterAccess
import tweepy
import staticDataStore

#This function takes a list of screennames and returns their ids
def returnIdsFromScreenNames(listofnames):
    listofids = []
    for name in listofnames:
        print(name)
        try:
            someuser = twitterAccess.api.get_user(screen_name=name)
            listofids.append(someuser.id)
        except:
            print("User does not exist")
    return listofids

def returnMostRecentTweet(somelistid):
    tweets = twitterAccess.api.list_timeline(owner='culturedcallie', list_id=somelistid)
    return tweets[0].id
