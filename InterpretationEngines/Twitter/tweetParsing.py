import NetworkXML
import re
import twitterAccess
import tweepy


#Look up mentions in that tweet data, and apply them
#to the XML file
#This function returns a list of lists. Each list in here will have the
#receiver and the giver's ids
def parseMentions(sometweet):
    listofMentionsInTweet = []
    sometweettext = sometweet.text
    mentionslist = re.findall("@[\w]*", sometweettext)
    namesToIds = NetworkXML.getAllAccountsNamesIDs()
    for mention in mentionslist:
        print(mention)
        #Firstly, check to see if it is in the dictionary of stuff
        #we already got
        if mention[1:] in namesToIds:
            print("SimpleLookup")
            gid = sometweet.user.id
            rid = int(namesToIds[mention[1:]])
            listofMentionsInTweet.append([rid, gid])
        else:
        #first, get that mention's iD
            try:
                rid = twitterAccess.api.get_user(screen_name=mention).id
                print(rid)
                #Then, get the tweeter's id
                gid = sometweet.user.id
                #the append is the receiver's id and the mention's id
                listofMentionsInTweet.append([rid, gid])
            except tweepy.error.TweepError as e:
                print("Error in finding user")
    return listofMentionsInTweet

#returns a gigantic list of receivers and givers
#takes in an allunredtweetdata
def getAllMentionsData(listOfTweets):
    bigMentionData = []
    for tweet in listOfTweets:
        mentionlist = parseMentions(tweet)
        for duo in mentionlist:
            bigMentionData.append(duo)
    return bigMentionData
