from . import Errors
from . import AnyPart
import math
import random

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
            return self.listOfParts[SearchID]
        else:
            raise Errors.NotInMemoryError(SearchID)

    def receiveNewPart(self, newPartID, newPartValue, dictOfConTypes):
        if len(self.listOfParts) >= self.LossLimit:
            #We stop the consuming, we cannot handle anything more
            raise OutOfMemoryError()
        else:
            if newPartID in self.listOfParts:
                raise RuntimeError("Part Already Exists")
            else:
                self.listOfParts[newPartID] = AnyPart.AnyPart(newPartID, newPartValue, dictOfConTypes)

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

    def getAnyPartID(self):
        somepartid = random.choice(list(self.listOfParts.keys()))
        return somepartid

    def prettyPrint(self):
        "PartMachine Pretty Print Initializing..."
        for key in self.listOfParts.keys():
            print("Key:" + key)
            listOfParts[key].prettyPrint()
            
            
