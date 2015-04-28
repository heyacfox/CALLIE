#THis is the over the top program, which runs on a schedule
#import readAllTimeline
import twitterAccess
#import re
import NetworkXML
import tweepy
import time
import writeXMLtoCSV
#import readTimelineFromXToY
import tweetParsing
import listInteractions
import staticDataStore
import twitterAccessUtilities
import lastReadTweetData
#Top Variables
#list id



#Pass him ALL THE DATA
def passUpdatestoXML(bigMentionsList):
    for mentionduo in bigMentionsList:
        NetworkXML.updateReceived(mentionduo[0], mentionduo[1])
    print("All Updates passed to XML")

def runSequenceOnce(addsize, somelistid, maxSize):
    mytweetdatastructure = listInteractions.allTweetDatafromList(somelistid)
    mymentionsdata = tweetParsing.getAllMentionsData(mytweetdatastructure)
    passUpdatestoXML(mymentionsdata)
    listInteractions.runArrangeWithTwitterActions(somelistid)
    NetworkXML.growSize(addsize, maxSize)

def runOnCadence(cadenceInSeconds, somelistid, addSizePerCadence, maxSize, restarthuh):
    if restarthuh:
        starttweet = twitterAccessUtilities.returnMostRecentTweet(somelistid)
        lastReadTweetData.rewriteLastID(starttweet)
    while True:
        runSequenceOnce(addSizePerCadence, somelistid, maxSize)
        print("SuccessfulSequence")
        try:
            writeXMLtoCSV.writeUsers()
            writeXMLtoCSV.writeReceivesThenGivenBy()
        except:
            print("Eh, I'll write it next time")
        print("Successful Write")
        mycadence = cadenceInSeconds
        while mycadence > 0:
            mycadence = mycadence - 1
            time.sleep(1)
            if mycadence%30 == 0:
                print("Time Remaining:" + str(mycadence))
        

def fullRestart(somelistid, userList):
    listInteractions.removeAllListMembers(somelistid)
    NetworkXML.rebootNetwork(len(userList)+1)
    listInteractions.followTheseIdsWithPatience(somelistid, twitterAccessUtilities.returnIdsFromScreenNames(userList), 30)
    listInteractions.setupBasicUsers(somelistid)

