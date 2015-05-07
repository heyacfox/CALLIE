#The connections class. Handles connections between parts

class ConnectionTypeList:
    typeID = ""
    listOfConnection = {}

    def __init__(self, newTypeID):
        self.typeID = newTypeID

    def addTypeConnection(self, newConnection):
        self.listOfConnection[newConnection.callieID] = newConnection
    
    
class Connection:
    callieMachine = ""
    callieID = ""
    weight = 1

    def __init__(self, newCallieMachine, newCallieID):
        self.callieMachine = newCallieMachine
        self.callieID = newCallieID

    def addWeight(self, value):
        self.weight = self.weight + value
    
