#This generates texts
from .. import PartMachine
from .. import Generator

class TextGenerator(Generator.Generator):
    lengthOfString = 0

    def __init__(self, newLengthOfString):
        self.lengthOfString = newLengthOfString

    #returns a list of strings, you decide what to do with them
    def generate(self):
        myPartMachine = self.partMachine
        return generateResultList(myPartMachine)

    def generateResultList(self, myPartMachine):
        newResultList = []
        initial = myPartMachine.getAnyPartID()
        newResultList.append(initial)
        currentLength = len(initial)
        return generateResultListRecursive(myPartMachine, newResultList, currentLength)

    def generateResultListRecursive(self, myPartMachine, newResultList, currentLength):
        #if we're at our string limit, slice the last thing off and call it a day
        if currentLength > self.lengthOfString:
            return newResultList[:-1]
        else:
            newID = newResultList[-1]
            newPart = myPartMachine.getPartByID(newID)
            if len(newPart.getAllConnectionsInType("Next")) > 0:
                #This is where where we check all our connections?
                myListOfConnectionsCopy = newPart.getAllConnectionsInType("Next").copy()
                #Now, we can wreck this list as needed
                try:
                    nextPartConnection = giveValidConnectionWithResult(myPartMachine, newPart)
                    newResultList.append(nextPartConnection.callieID)
                    currentLength = currentLength + len(nextPartConnection.callieID)
                    generateResultListRecursive(myPartMachine, newResultList, currentLength)
                except NoValidConnectionsError:
                    #There are no valid next connections for this part
                    if len(newResultList) == 1:
                        generateREsultList(myPartMachine)
                    else:
                        generateResultListRecursive(self, myPartMachine, newResultList[:-1], currentLength - len(newResultList[-1]))
                


                
            else:
                #if there are no connections we can use, check if we're the last thing
                if len(newResultList) == 1:
                    #then start from the top
                    generateResultList(myPartMachine)
                else:
                    #if we are NOT the last thing, just go back an element and try again
                    generateResultListRecursive(self, myPartMachine, newResultList[:-1], currentLength - len(newResultList[-1]))
                    
            #if there are connections we can use
            #We need to create a duplicate of that thing and pop each element off
            #that we can't use, until we get to nothing


            #if we are killing off the last item in our result list, go back to generate result list

    
        
    def giveValidConnectionWithResult(self, myPartMachine, myPart):
        #this function goes through allthe next connections, and will eventually return one that is valid. Hopefully
        partDestructor = myPart.copy()
        potentialConnections = partDestructor.getAllConnectionsInType("Next")
        while len(potentialConnections.keys()) > 0:
            newConnection = partDestructor.returnWeightedRandomConnectionInType("Next")
            try:
                newResult = myPartMachine.getPartByID(newConnection.callieID)
                return newConnection
            except NotInMemoryError:
                removed = partDestructor.ListOfConnectionTypes["Next"].pop(newConnection.callieID)
                potentialConnections = partDestructor.LIstOfConnectionTypes["Next"]
            
                
