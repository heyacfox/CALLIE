import tweepy
import unicodedata
import codecs
import PyReadToXML
access_token = "2980642296-DhGM52aqKOiv1ujIgbxOdOCc1g8DgSoi9LnAFXT"
access_token_secret = "YaVrJNeEdp7O5ulWkXmbzcSzS4JkK85BWgQvN2Qq95Pat"
consumer_key =  "ES9oS0bpmdZQHhje1XrfPpqFx"
consumer_secret = "sUucyVHDSCjKtMWzf6K7h5S77k6XTgFwZrHrFQG7ShcO5JyEdW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

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
mytrends = api.trends_place(23424977)[0]['trends']
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
        """
        try:
            encodedtext.decode('utf-8')
        except UnicodeDecodeError:
            valid_utf8 = False
        if valid_utf8:
            print("Text" + encodedtext.decode('utf-8'))
        else:
            print("Text Invalid")
        """
        try:
            print("Text:" + encodedtext.decode('utf-8', errors='ignore'))
            lott.append(encodedtext.decode('utf-8', errors='ignore'))
        except UnicodeEncodeError:
            print("Error Occurred")
    
print("endoftrends")

PyReadToXML.readStringList(lott, "CALLIEMachine.xml")
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

#return 

def main():
    

main()
