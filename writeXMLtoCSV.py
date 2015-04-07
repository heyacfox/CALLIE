import NetworkXML
import csv

def writeUsers():
    biglist = []
    for x in NetworkXML.listOfCoreNetwork():
        biglist.append(x)
    for y in NetworkXML.listOfExtendedNetwork():
        biglist.append(y)
    writingList = []
    writingList.append(["Id", "Label", "Status", "Total"])
    for z in biglist:
        #print(str(z))
        basicUser = []
        basicUser.append(str(z))
        basicUser.append(NetworkXML.getNetworkElementValue(int(z), "Username"))
        basicUser.append(NetworkXML.getNetworkElementValue(int(z), "Status"))
        basicUser.append(str(NetworkXML.totalmentionsobject(int(z)).mentionsreceived))
        #print(basicUser)
        writingList.append(basicUser)
    resultFile = open("ListOfNetwork.csv", 'w', newline='')
    wr = csv.writer(resultFile, dialect='excel')
    #print(writingList)
    wr.writerows(writingList)

def writeReceivesThenGivenBy():
    biglist=[]
    hugelist=[]
    actualwritinglist=[]
    actualwritinglist.append(["Source", "Target", "Weight"])
    for x in NetworkXML.listOfCoreNetwork():
        biglist.append(x)
    for y in NetworkXML.listOfExtendedNetwork():
        biglist.append(y)
    #this z is the string ids of people in the network list
    for z in biglist:
        #in huge list, we put the receivers id with the list of givers ids
        listofreceives = NetworkXML.getUsersReceives(int(z))
        hugelist.append([z, listofreceives])
    for q in hugelist:
    #(we need to reformat this into rows)
        for receive in q[1]:
            actualwritinglist.append([receive[0], q[0], receive[1]])
    #print(actualwritinglist)
    resultFile = open("ListOfGivesReceives.csv", 'w', newline='')
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(actualwritinglist)
        
        
