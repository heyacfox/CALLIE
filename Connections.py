#The connections class. Handles connections between parts

class ConnectionTypeList:
    typeID = ""
    listOfConnection = {}

    def __init__(self, newTypeID):
        self.typeID = newTypeID

    def addTypeConnection(self, newConnection):
        listOfConnection[newConnection.callieID] = newConnection
    
    
class Connection:
    callieMachine = ""
    callieID = ""
    weight = 0

    def __init__(self, newCallieMachine, newCallieID):
        self.callieMachine = newCallieMachine
        self.callieID = newCallieID

    def addWeight(self, value):
        self.weight = self.weight + value
    
