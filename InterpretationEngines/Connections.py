#The connections class. Handles connections between parts

class ConnectionTypeList:
    typeID = ""
    listOfConnection = {}

    def __init__(self, newTypeID):
        self.typeID = newTypeID

    def addTypeConnection(self, newConnection):
        self.listOfConnection[newConnection.PartID] = newConnection

    def PrettyPrinting(self):
        print("Pretty Print Initalized for ConnectionTypeList: " + self.typeID)
        for key in self.listOfConnection.keys():
            print("Key: " + key + "|Weight: " + str(self.listOfConnection[key].weight))
            
    

#Why the eff do connections need to access the Callie Machine? They are WAY too
#low level to even BEGIN touching something like that. 
class Connection:
    callieMachineStrRef = ""
    PartID = ""
    weight = 1

    def __init__(self, newCallieMachine, newPartID):
        self.callieMachineStrRef = newCallieMachine
        self.PartID = newPartID

    def addWeight(self, value):
        self.weight = self.weight + value
    
