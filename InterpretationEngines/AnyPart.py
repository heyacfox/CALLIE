#Part Class
from . import Constants
import random

class AnyPart:
    PartID = ""
    PartValue = ""
    ListOfConnectionTypes = {}
    
    def __init__(self, myID, myValue, dictionaryOfConTypes):
        self.PartID = myID
        self.PartValue = myValue
        self.ListOfConnectionTypes = dictionaryOfConTypes

    def addConnection(self, TypeListID, newConnection):
        if TypeListID in self.ListOfConnectionTypes:
            if newConnection.PartID in self.ListOfConnectionTypes[TypeListID].listOfConnection:
                #print("Anypart: Added Weight")
                self.ListOfConnectionTypes[TypeListID].listOfConnection[newConnection.PartID].addWeight(Constants.weightToAdd)
            else:
                #print("Anypart: Made new connection")
                self.ListOfConnectionTypes[TypeListID].addTypeConnection(newConnection)
        else:
            raise RuntimeError('Not in types')

    def returnRandomConnection(self):
        newDictionary = random.choice(list(self.ListOfConnectionTypes.keys()))
        newConnection = random.choice(list(newDictionary.keys()))
        return newConnection

    def returnRandomConnectionInType(self, typeSearchID):
        newConnection = random.choice(self.ListOfConnectionTypes[typeSearchID].keys())
        return newConnection

    def returnWeightedRandomConnectionInType(self, typeSearchID):
        totallyNewDictionary = self.ListOfConnectionTypes[typeSearchID].copy()
        totalWeight = 0
        for key, value in totallyNewDictionary:
            totalWeight = totalWeight + value.weight
        #after we have generated our total connection weights, we can do the breakdown
        randomWeight = random.randint(1, totalWeight - 1)
        for key, value in totallyNewDictionary:
            randomWeight = randomWeight - value.weight
            if randomWeight < 0:
                return value

    def returnTotalConnectionWeight(self):
        totalConnectionsAndWeights = 0
        for x in selfListOfConnectionTypes.values():
            for y in x.values():
                totalConnectionsAndWeights = totalConnectionsAndWeights + y.weight
        return totalConnectionsAndWeights


    def hasConnectionHuh(self, somePartID):
        raise RuntimeError()


    def hasConnectionHuhInType(self, somePartID, someType):
        if someType in self.ListOfConnectionTypes:
            if somePartID in self.ListOfConnectionTypes[someType].listOfConnection:
                return True
        return False

    def getConnectionInType(self, somePartID, someType):
        return self.ListOfConnectionTypes[someType].listOfConnection[somePartID]

    #returns ALL CONNECTION KEYS MAKE SURE YOU WANT THIS
    def getAllConnectionsInType(self, someType):
        return self.ListOfConnectionTypes[someType].keys()

    def prettyPrint(self):
        print(self.PartValue)

