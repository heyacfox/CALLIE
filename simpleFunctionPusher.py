import NetworkBuilderSequence
import staticDataStore
import listInteractions
import twitterAccessUtilities

def restartingNetwork():
    templistid = staticDataStore.FurryNetworkID
    userList = listInteractions.returnUsersNamesMatchFromTerms(
        listInteractions.returnUsersInList(staticDataStore.FurryNetworkID),
        staticDataStore.listOfFurryTerms)
    #userList = staticDataStore.listOfFurCons
    #userList = staticDataStore.tempfurrylist
    
    NetworkBuilderSequence.fullRestart(templistid,userList)
    print("Complete")

def myRunCadence():
    sec = 120
    listid = staticDataStore.FurryNetworkID
    addsize = 1
    maxSize = 150
    restarthuh = True
    NetworkBuilderSequence.runOnCadence(sec, listid, addsize, maxSize, restarthuh)
                                                             
def cadenceWithReboot(betweenCadence, cadenceBetweenReboot):
    print("X")
