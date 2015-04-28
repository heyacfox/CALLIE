import PyReadToXML
import PyWriteFromXML
import tweepytwitter

import tweepy
import unicodedata
import codecs
import time
access_token = "2980642296-DhGM52aqKOiv1ujIgbxOdOCc1g8DgSoi9LnAFXT"
access_token_secret = "YaVrJNeEdp7O5ulWkXmbzcSzS4JkK85BWgQvN2Qq95Pat"
consumer_key =  "ES9oS0bpmdZQHhje1XrfPpqFx"
consumer_secret = "sUucyVHDSCjKtMWzf6K7h5S77k6XTgFwZrHrFQG7ShcO5JyEdW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True)

ListofStringsToRead = ["Hello, my name is @Jane",
                       "I have one hundred cows",
                       "I can't #believe she said that to me",
                       "I want a #muffin",
                       "Long string list that has a lot of @things and is not easily comprehended",
                       "Somename of someone",
                       "Heyo http://twitter.com"
                       "http://t.co.skdljfnaslkjdbn"]
"""
PyReadToXML.readStringList(ListofStringsToRead, "CallieMachine.xml")
print("readStringList test passed")

PyReadToXML.readTextFile("somestory.txt", "CallieMachine.xml")
print("ReadTextFileComplete")

"""
#print(PyWriteFromXML.writeString(4000, "CallieMachine.xml"))





#PyReadToXML.readFilesInFolder("txtstoread", "CallieMachine.xml")

#mynewstring = tweepytwitter.purgeSymbolsFromList(ListofStringsToRead)

#print(mynewstring)
def addtolist():
    for page in tweepy.Cursor(api.followers, screen_name="homphs").pages():
        for f in page:
            try:
                print(f.screen_name)
                print(f.id)
                #if not (api.is_list_member(cultured_callie, '189208099',f.id)):
                api.add_list_member(list_id='189208099', user_id=f.id)
                print("Added User")
            except tweepy.error.TweepError as e:
                print("Sleeping for a while")
                #print(e.response.status)
                print(str(api.rate_limit_status()))
                time.sleep(5)


def goaddtolistmanage():
    while True:
        try:
            addtolist()
        except tweepy.error.TweepError:
            print("Sleeping for a while")
            time.sleep(60)

#goaddtolistmanage()
"""
tweets = api.list_timeline(owner='culturedcallie', list_id='189208099')
for t in tweets:
    encodedtext = t.text.encode("utf-8", errors='ignore')
    print("Text:" + encodedtext.decode('utf-8', errors='ignore'))
"""
"""
mylists = api.lists_all()
for x in mylists:
    print(str(x.id))
    print(x.name)
    """
#kagefollowers = api.followers('UncleKage', -1)

print(tweepytwitter.removeLinksFromList(ListofStringsToRead))


