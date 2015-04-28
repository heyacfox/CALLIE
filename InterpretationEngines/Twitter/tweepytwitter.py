import tweepy
import unicodedata
import codecs
import PyReadToXML
import PyWriteFromXML
import time
import re
access_token = "2980642296-DhGM52aqKOiv1ujIgbxOdOCc1g8DgSoi9LnAFXT"
access_token_secret = "YaVrJNeEdp7O5ulWkXmbzcSzS4JkK85BWgQvN2Qq95Pat"
consumer_key =  "ES9oS0bpmdZQHhje1XrfPpqFx"
consumer_secret = "sUucyVHDSCjKtMWzf6K7h5S77k6XTgFwZrHrFQG7ShcO5JyEdW"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
"""
#public_tweets = api.search("Coyote")
public_tweets = api.home_timeline()
#public_tweets = api.user_timeline('@heyacfox')
for tweet in public_tweets:
    encodedtext = tweet.text.encode("utf-8", errors='ignore')
    #print(tweet.user.name)
    encodeduser = tweet.user.name
    print("Name:" + encodeduser)
    print("Text:" + encodedtext.decode('utf-8'))



#returns a list with all followers
def buildFollowerList():
    myfollowers = api.followers()
    followerlist = []
    for f in myfollowers:
        followerlist.append(f.id)
    return followerlist
        


def inFollowerListHuh(userid):
    myfollowerlist = buildFollowerList()
    if userid in myfollowerlist:
        return True
    else:
        return False
    
mentions = api.mentions_timeline()

print("Mentions")
"""
"""
for tweet in mentions:
    encodedtext = str(tweet.text)
    encodeduser = tweet.user.name
    print("Name:" + encodeduser)
    print("Text:" + encodedtext)
    print("ID" + str(tweet.user.id))
    if 'follow me' in encodedtext.lower():
        print("found a follow me")
        #if 'unfollow me' not in encodedtext.lower():
        #if not inFollowerListHuh(tweet.user.id):
        #    api.create_friendship(tweet.user.id)
        #    print("followedsomeone")
        #else:
        #print("Found unfollow me inside the follow me")
        isfollowinghuh = api.get_user(tweet.user.id).following
        if not isfollowinghuh:
            api.create_friendship(tweet.user.id)
            print("Followed someone")
    if 'unfollow me' in encodedtext.lower():
        api.destroy_friendship(tweet.user.id)
        print("Unfollowed someone")
    print("endoftweet")
    """
"""
for trend in mytrends:
    print(trend['name'])
    print(trend['query'])
    myreturntweets = api.search(trend['query'])
    lott = []
    for qreturn in myreturntweets:
        encodedtext = qreturn.text.encode('utf-8', errors='ignore')
        encodeduser = qreturn.user.screen_name
        print("Name:" + encodeduser)
        valid_utf8 = True
        
        try:
            encodedtext.decode('utf-8')
        except UnicodeDecodeError:
            valid_utf8 = False
        if valid_utf8:
            print("Text" + encodedtext.decode('utf-8'))
        else:
            print("Text Invalid")
        
        try:
            print("Text:" + encodedtext.decode('utf-8', errors='ignore'))
            lott.append(encodedtext.decode('utf-8', errors='ignore'))
        except UnicodeEncodeError:
            print("Error Occurred")
    
print("endoftrends")

PyReadToXML.readStringList(lott, "CALLIEMachine.xml")
"""
"""
{
 'contributors': None,
 'truncated': False,
 'text': 'My Top Followers in 2010: @tkang1 @serin23 @uhrunland @aliassculptor @kor0307 @yunki62. Find yours @ http://mytopfollowersin2010.com',
 'in_reply_to_status_id': None,
 'id': 21041793667694593,
 '_api': <tweepy.api.api object="" at="" 0x6bebc50="">,
 'author': <tweepy.models.user object="" at="" 0x6c16610="">,
 'retweeted': False,
 'coordinates': None,
 'source': 'My Top Followers in 2010',
 'in_reply_to_screen_name': None,
 'id_str': '21041793667694593',
 'retweet_count': 0,
 'in_reply_to_user_id': None,
 'favorited': False,
 'retweeted_status': <tweepy.models.status object="" at="" 0xb2b5190="">,
 'source_url': 'http://mytopfollowersin2010.com',
 'user': <tweepy.models.user object="" at="" 0x6c16610="">,
 'geo': None,
 'in_reply_to_user_id_str': None,
 'created_at': datetime.datetime(2011, 1, 1, 3, 15, 29),
 'in_reply_to_status_id_str': None,
 'place': None
}
"""


#re

#Runs the read to CallieMachine
def putInMachine(ListOfString, CM):
    slist = purgeSymbolsFromList(ListOfString)
    PyReadToXML.readStringList(slist, CM)

#returns a list of strings that are the home timeline tweets not yet read
def readHomeTimeline():
    ListOfString = []
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        try:
            encodedtext = tweet.text.encode("utf-8", errors='ignore')
            print("Text:" + encodedtext.decode('utf-8', errors='ignore'))
            ListOfString.append(encodedtext.decode('utf-8', errors='ignore'))
        except UnicodeEncodeError:
            print("Read Home Error")
    return ListOfString

#returns a list of strings that are some trend tweets not read
def readTrendTimeline():
    ListOfString = []
    mytrends = api.trends_place(23424977)[0]['trends']
    for trend in mytrends:
        myreturntweets = api.search(trend['query'])
        for qreturn in myreturntweets:
            encodedtext = qreturn.text.encode('utf-8', errors='ignore')
            encodeduser = qreturn.user.screen_name
            print("Name:" + encodeduser)
            try:
                print("Text:" + encodedtext.decode('utf-8', errors='ignore'))
                ListOfString.append(encodedtext.decode('utf-8', errors='ignore'))
            except UnicodeEncodeError:
                print("Error Occurred")
    return ListOfString

#Checks mentions and follows and unfollows based on that
def CheckMentionFollowUnfollow():
    mentions = api.mentions_timeline()
    for tweet in mentions:
        try:
            encodedtext = tweet.text.encode('utf-8', errors='ignore')
            if 'follow me' in encodedtext.decode('utf-8').lower():
                isfollowinghuh = api.get_user(tweet.user.id).following
                if not isfollowinghuh:
                    api.create_friendship(tweet.user.id)
            if 'unfollow me' in encodedtext.decode('utf-8').lower():
                api.destroy_friendship(tweet.user.id)
        except UnicodeEncodeError:
            print("UnicodeError")
            
#removes @ and # from strings in a list of strings, returns list of strings
def purgeSymbolsFromList(ListOfString):
    los = ListOfString
    newlos = []
    for s in los:
        new = s.replace('#', '')
        newtoo = new.replace('@', '')
        newlos.append(newtoo)
    return newlos

def readStatusFromList():
    tweets = api.list_timeline(owner='culturedcallie', list_id='189208099')
    ListOfString = []
    for t in tweets:
        try:
            encodedtext = t.text.encode("utf-8", errors='ignore')
            print("Text:" + encodedtext.decode('utf-8', errors='ignore'))
            ListOfString.append(encodedtext.decode('utf-8', errors='ignore'))
        except UnicodeEncodeError:
            print("Read Home Error")
    return ListOfString
        
def removeLinksFromList(ListOfString):
    newLOS = []
    for mys in ListOfString:
        mytext = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}     /)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', mys)
        newLOS.append(mytext)
    return newLOS

#updatesStatusFromTweets
def updateStatusFromTweets():
    mytweet = PyWriteFromXML.writeString(120, "CallieMachineFurry.xml")
    print("Tweet:" + mytweet)
    api.update_status(mytweet)

def mainonxtime():
    try:
        #CheckMentionFollowUnfollow()
        #putInMachine(purgeSymbolsFromList(readHomeTimeline()), "CallieMachine.xml")
        #putInMachine(purgeSymbolsFromList(readTrendTimeline()), "CallieMachine.xml")
        putInMachine(removeLinksFromList(purgeSymbolsFromList(readStatusFromList())), "CALLIEMachineFurry.xml")
        updateStatusFromTweets()
    except tweepy.error.TweepError as te:
        print(te.response)
        print(te.reason)
        print("Error Occured")
        time.sleep(3600)
    time.sleep(3600)

def beginprocess():
    while True:
        mainonxtime()
    
