#Part Class
import Constants
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
        if TypeListID in ListOfConnectionTypes:
            if newConnection.callieID in ListOfConnectionTypes[TypeListID].listOfConnection:
                ListOfConnectionTypes[TypeListID].listOfConnection[newConnection.callieID].addWeight(Constants.weightToAdd)
            else:
                ListOfConnectionTypes[TypeListID].addTypeConnection(newConnection)
        else:
            raise Error('Not in types')

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
            
