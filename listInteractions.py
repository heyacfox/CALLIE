import NetworkXML
import tweepy
import twitterAccess
import readAllTimeline
import time

#Based on the returned information on who is now core and who is now extended,
#Add or remove people from the list
def unFollowTheseIds(somelistid, listofids):
    for myid in listofids:
        print("UnFollowed:" + str(myid))
        twitterAccess.api.remove_list_member(list_id=somelistid, id=myid)

def followTheseIds(somelistid, listofids):
    for myid in listofids:
        print("Followed:" + str(myid))
        twitterAccess.api.add_list_member(list_id=somelistid, id=myid)

def removeAllListMembers(somelistid):
    for page in tweepy.Cursor(twitterAccess.api.list_members, owner='culturedcallie', list_id=somelistid).pages():
        for member in page:
            print("Member:" + str(member.id))
            twitterAccess.api.remove_list_member(list_id=somelistid, id=member.id)

#First, get all the unread tweet data. Returns a list of tweet objects?
def allTweetDatafromList(somelistid):
    return readAllTimeline.pullAllNonReadTweetsFromListTimeline(somelistid)

#Sets up the initial people in the list in the XML
def setupBasicUsers(somelistid):
    for page in tweepy.Cursor(twitterAccess.api.list_members, owner='culturedcallie', list_id=somelistid).pages():
        for someuser in page:
            NetworkXML.addUserToNetworkStart(someuser.id, someuser.screen_name)
    print("Users set up")

def returnAllListIds(somelistid):
    listIds = []
    for page in tweepy.Cursor(twitterAccess.api.list_members, owner="culturedcallie", list_id=somelistid).pages():
        for user in page:
            listIds.append(user.id)
    return listIds

def followCoreUsers(somelistid, waitInBetween, listIdsFromTwitter):
    #This makes sure that all core users are followed. Should
    #only be used in the case of an error in the sequence in the rearranging users step
    myCoreIds = NetworkXML.listOfCoreNetwork()
    currentlist = listIdsFromTwitter
    print("Sleeping for " + str(waitInBetween) + " to give some breathing room")
    time.sleep(waitInBetween)
    errorTrigger = "Success"
    for myid in myCoreIds:
        try:
            if int(myid) in currentlist:
                print("Already Here")
            else:
                twitterAccess.api.add_list_member(list_id=somelistid, id=int(myid))
                print("Added user:" + myid)
        except tweepy.error.TweepError as e:
            print("Crashed on User id:" + myid)
            print(e.response)
            errorTrigger = "NotAllSuccess"
    return errorTrigger

def followCoreWithErrorCheck(somelistid):
    waittime = 0
    twitterListIds = returnAllListIds(somelistid)
    while followCoreUsers(somelistid, waittime, twitterListIds) == "NotAllSuccess":
        print("Failure")
        waittime = waittime + 30
        #increases wait time by 30 seconds every run so that I am sure I got EVERYTHING
    print("SuccessfullyDoneWithNoErrors")

#Rearrange the CORE and EXTENDED users
def runArrangeWithTwitterActions(somelistid):
    myActionList = NetworkXML.reArrangeCoreAndExtended()
    myFollowList = []
    myUnfollowList = []
    for x in myActionList:
        if x[1] == "ToExt":
            myUnfollowList.append(x[0])
        elif x[1] == "ToCore":
            myFollowList.append(x[0])
    unFollowTheseIds(somelistid, myUnfollowList)
    try:
        followTheseIds(somelistid, myFollowList)
    except tweepy.error.TweepError:
        followCoreWithErrorCheck(somelistid)

def returnOnePageOfEarliestListTweetsFromId(myowner, startId, someListId):
    mypages = twitterAccess.api.list_timeline(owner=myowner, list_id=someListId, since_id=startId)
    
    
def followTheseIdsWithPatience(somelistid, listofids, waittime):
    errorList = []
    for myid in listofids:
        try:
            twitterAccess.api.add_list_member(list_id=somelistid, id=myid)
            print("Followed:" + str(myid))
        except tweepy.error.TweepError as e:
            print("Crashed on User id:" + str(myid))
            print(e.response)
            errorList.append(myid)
    if len(errorList) > 0:
        print("Errored, waiting for: " + str(waittime))
        print(errorList)
        time.sleep(waittime)
        followTheseIdsWithPatience(somelistid, errorList, waittime + 30)

#returns a list of USER objects from a given listID
def returnUsersInList(somelistid):
    userslist = []
    for page in tweepy.Cursor(twitterAccess.api.list_members, owner='culturedcallie', list_id=somelistid).pages():
        for user in page:
            print(user.screen_name)
            print(user.id)
            userslist.append(user)
    return userslist

#returns a list of users that match from the list
def returnUsersNamesMatchFromTerms(usersobjlist, termslist):
    goodusersnames = []
    for userx in usersobjlist:
        userscreenname = userx.screen_name
        userid = userx.id
        userdes = userx.description
        usertempname = userx.name
        userdata = userscreenname + usertempname + userdes
        for term in termslist:
            if term in userdata:
                print("Matched Terms:" + userscreenname)
                goodusersnames.append(userscreenname)
                break
    print(goodusersnames)
    return goodusersnames
