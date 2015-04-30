import Errors
import AnyPart
import math

#This is the dataStorageClass

class PartMachine:
    #Parts is a dictionary, because there is an ID for everything I need.
    #The connections are handled internally after the part is retrieved
    listOfParts = {}
    LossLimit = 0
    MaxExpansionPercentage = 0.0

    def __init__(self, startLossLimit, startExpansionPercentage):
        self.LossLimit = startLossLimit
        self.MaxExpansionPercentage = startExpansionPercentage

    #a public function that will return a part from the list based 
    def getPartByID(self, SearchID):
        if SearchID in self.listOfParts:
            return listOfParts[SearchID]
        else:
            raise Errors.NotInMemoryError(SearchID)

    def receiveNewPart(self, newPartID, newPartValue):
        if len(listOfParts) >= LossLimit:
            #We stop the consuming, we cannot handle anything more
            raise OutOfMemoryError()
        else:
            if newPartID in listOfParts:
                raise Error("Part Already Exists")
            else:
                listOfParts[newPartID] = AnyPart(newPartID, newPartValue)

    def initiateLossyMemoryExpansion(self):
        #create a list fro the listOfParts dictionary
        newList = self.listOfParts.values()
        #Sort the list by the amount of connections the parts have
        newList.sort(key=lambda x: x.returnTotalConnectionWeight(), reverse=True)
        #remove MaxExpansionPercentage % of the list, record that number
        numberToRemove = math.floor(float(LossLimit) * MaxExpansionPercentage)
        listToRemove = newList[:(numberToRemove - 1)]
        for x in listToRemove:
            removed = self.listOfParts.pop(x.callieID)
        #Add that number to the LossLimit
        self.LossLimit = self.LossLimit + numberToRemove
        return "X"

    def consumeData(self, data):
        return "X"
            
