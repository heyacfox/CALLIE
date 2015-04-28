import xml.etree.ElementTree as ET
import twitterAccess
import time
#The XML Structure
"""


The NetworkList is all the users in the core network: the List of 500 users.

The NetworkBotList is all the users that have been pinged, but they are not in
the core 500, so we do not read their tweets.

The DoNo
"""

#global maxListSize
#maxListSize = 0

class tempuser:
    tempuserid = 0
    mentionsreceived = 0

    def __init__(self, myid, mytotal):
        self.tempuserid = myid
        self.mentionsreceived = mytotal



#This function will return the tree which you can edit as you like
def pullNetworkXML():
    tree = ET.parse("NetworkList.xml")
    return tree

#This function returns the list of everyone by id in the core network
def listOfCoreNetwork():
    mytree = pullNetworkXML()
    root = mytree.getroot()
    coreNetworkListXML = root[0]
    myCoreList = []
    for child in coreNetworkListXML:
        if child[2].text == "Core":
            myCoreList.append(child[0].text)
    return myCoreList

#This function returns the list of everyone in the extended network
def listOfExtendedNetwork():
    mytree = pullNetworkXML()
    root = mytree.getroot()
    extendedNetworkListXML = root[0]
    myExtendedList = []
    for child in extendedNetworkListXML:
        if child[2].text == "Extended":
            myExtendedList.append(child[0].text)
    return myExtendedList

#This updates a network element variable value
def updateNetworkElement(identifier, variable, value):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    accounts = root[0]
    for a in accounts:
        if int(a[0].text) == identifier:
            a.find(variable).text = value
            print("Value Updated")
    saveNetwork(mytree)
    

#This gets a network element variable value. Identifier is an integer
    #variable is a string???
def getNetworkElementValue(identifier, variable):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    accounts = root[0]
    for a in accounts:
        if int(a[0].text) == identifier:
            return a.find(variable).text
    print("THAT VARIABLE DOES NOT EXIST")

def updateReceived(receiverid, giverid):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    accounts = root[0]
    giverFound = False
    receiverFound = False
    for a in accounts:
        if int(a[0].text) == receiverid:
            receiverFound = True
            for giver in a[3][1]:
                if int(giver[0].text) == giverid:
                    giver[1].text = str(int(giver[1].text) + 1)
                    a[3][0].text = str(int(a[3][0].text)+1)
                    giverFound = True
                    print("Updated Existing Giver")
            if giverFound == False:        
                #IF we reach here, there was no giver that matched that ID
                mynewgiver = ET.SubElement(a[3][1], "AccountFrom")
                mynewgiverid = ET.SubElement(mynewgiver, "Id")
                mynewgiveramount = ET.SubElement(mynewgiver, "Amount")
                mynewgiverid.text = str(giverid)
                mynewgiveramount.text = "1"
                a[3][0].text = str(int(a[3][0].text)+1)
                print("Added new giver")
            saveNetwork(mytree)
    #We get here at the end no matter what
    if receiverFound == False:
        addUserToNetwork(receiverid, twitterAccess.api.get_user(receiverid).screen_name, giverid)
                    
                    
#return total mentions user object from an id
def totalmentionsobject(userid):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    accounts = root[0]
    for a in accounts:
        if int(a[0].text) == userid:
            return tempuser(userid, int(a[3][0].text))
            

#moves someone from the core list to the extended list in the xml
def coreToExtended(identifier):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    updateNetworkElement(identifier, "Status", "Extended")

#moves someone from the extended list to the core list in the xml
def extendedToCore(identifier):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    updateNetworkElement(identifier, "Status", "Core")

#Adds a user to the network in the EXTENDED status, it's up to you
#to rearrange these if you want.
def addUserToNetwork(identifier, username, giverid):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    mynewaccount = ET.SubElement(root[0], "Account")
    mynewaccountid = ET.SubElement(mynewaccount, "Id")
    mynewaccountid.text = str(identifier)
    mynewusername = ET.SubElement(mynewaccount, "Username")
    mynewusername.text = username
    mynewaccountstatus = ET.SubElement(mynewaccount, "Status")
    mynewaccountstatus.text = "Extended"
    mynewaccountmentions = ET.SubElement(mynewaccount, "MentionsReceived")
    mynewaccountmentionstotal = ET.SubElement(mynewaccountmentions, "Total")
    mynewaccountmentionstotal.text = "0"
    mynewaccountmentionsbyaccount = ET.SubElement(mynewaccountmentions, "ByAccount")
    saveNetwork(mytree)
    print("Added User")
    updateReceived(identifier, giverid)
    print("UpdatedNewUser")

#Adds a user to the network in the EXTENDED status, it's up to you
#to rearrange these if you want.
def addUserToNetworkStart(identifier, username):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    mynewaccount = ET.SubElement(root[0], "Account")
    mynewaccountid = ET.SubElement(mynewaccount, "Id")
    mynewaccountid.text = str(identifier)
    mynewusername = ET.SubElement(mynewaccount, "Username")
    mynewusername.text = username
    mynewaccountstatus = ET.SubElement(mynewaccount, "Status")
    mynewaccountstatus.text = "Extended"
    mynewaccountmentions = ET.SubElement(mynewaccount, "MentionsReceived")
    mynewaccountmentionstotal = ET.SubElement(mynewaccountmentions, "Total")
    mynewaccountmentionstotal.text = "0"
    mynewaccountmentionsbyaccount = ET.SubElement(mynewaccountmentions, "ByAccount")
    saveNetwork(mytree)
    print("Added User")

#saves the network
def saveNetwork(tree):
    tree.write("NetworkList.xml")

#This takes the list of accounts and makes sure the top 500 accounts are the
#core, and everyone else is considered extended.
def reArrangeCoreAndExtended():
    #Get the entire List
    biguserlist = []
    coreuserlist = listOfCoreNetwork()
    extuserlist = listOfExtendedNetwork()
    for x in coreuserlist: 
        biguserlist.append(x)
    for y in extuserlist:
        biguserlist.append(y)
    #print(biguserlist)
    #Set up the structure so we have each person and their total received
    biguserlistwithcount = makeUserObjects(biguserlist)
    #order the list from 0 is largest to the last one is smallest
    #print(biguserlistwithcount)
    biguserlistwithcount.sort(key=lambda x: x.mentionsreceived, reverse=True)
    actionlist = []
    #don't split the list if it is less than 499 people
    mytree = pullNetworkXML()
    root = mytree.getroot()
    maxListSize = int(root[1].text)
    if len(biguserlistwithcount) < maxListSize:
        for user in biguserlistwithcount:
            #check if in core
            if getNetworkElementValue(user.tempuserid, "Status") == "Extended":
                extendedToCore(user.tempuserid)
                actionlist.append([user.tempuserid, "ToCore"])
                
            #if not in core, put them in core and add to the result list
    else:
        topslice = biguserlistwithcount[:(maxListSize - 1)]
        bottomslice = biguserlistwithcount[(maxListSize - 1):]
        print("NotWrittenYet")
    #split the list in two
    #for each list
        for userobj in topslice:
            if getNetworkElementValue(userobj.tempuserid, "Status") == "Extended":
                extendedToCore(userobj.tempuserid)
                actionlist.append([userobj.tempuserid, "ToCore"])
        for userobj in bottomslice:
            if getNetworkElementValue(userobj.tempuserid, "Status") == "Core":
                coreToExtended(userobj.tempuserid)
                actionlist.append([userobj.tempuserid, "ToExt"])
        #check to see if the user matches what they should be
        #If not, change their data and add them to the feedback list
    #return the feedback list
    print("EndOfActionListCreation")
    return actionlist


def makeUserObjects(listofids):
    objectlist = []
    for myid in listofids:
        myobj = totalmentionsobject(int(myid))
        objectlist.append(myobj)
    return objectlist

#returns a list of tuples. First in the tuple is the id, second is
#how many times it was received by. id is returned as string, both are
#returned as strings
#pass in someid as an integer please
def getUsersReceives(someid):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    accounts = root[0]
    bigtuplelist = []
    for a in accounts:
        if int(a[0].text) == someid:
            for x in a[3][1]:
                xpart1 = x[0].text
                xpart2 = x[1].text
                bigtuplelist.append([xpart1, xpart2])
    return bigtuplelist

def getAllAccountsIDsNames():
    mytree = pullNetworkXML()
    root = mytree.getroot()
    accounts = root[0]
    bigdictionary = dict()
    for a in accounts:
        myid = a[0].text
        myname = a[1].text
        bigdictionary[myid] = myname
    return bigdictionary

def getAllAccountsNamesIDs():
    mytree = pullNetworkXML()
    root = mytree.getroot()
    accounts = root[0]
    bigdictionary = dict()
    for a in accounts:
        myid = a[0].text
        myname = a[1].text
        bigdictionary[myname] = myid
    return bigdictionary

def rebootNetwork(coreSize):
    mytime = str(time.time())
    newfilepath = "Archive/NetworkList_" + mytime + ".xml"
    oldfilepath = "NetworkList.xml"
    import shutil
    shutil.copy2(oldfilepath, newfilepath)
    root = ET.Element("root")
    doc = ET.SubElement(root, "NetworkList")
    mysize = ET.SubElement(root, "CoreSize")
    mysize.text = str(coreSize)
    tree = ET.ElementTree(root)
    tree.write("NetworkList.xml")

def growSize(addSize, maxSize):
    mytree = pullNetworkXML()
    root = mytree.getroot()
    mysize = root[1]
    if int(mysize.text) < maxSize:
        mysize.text = str(int(mysize.text) + addSize)
    saveNetwork(mytree)
