#THis is the CallieMachine Class. All other CallieMachines must
#inherit from this design

class CallieMachine:
    dataStorageLocation = ""
    dataStorageClass = ""

    def __init__(self, newDataStorageLocation):
        dataStorageLocation = newDataStorageLocation
        dataStorageClass = returnClassFromData(dataStorageLocation)

    #this must be implemented on every machine
    def returnClassFromData(self):
        return False

    def saveClassToData(self):
        return False

    def consumeContent(self, contentLocation):
        return False

    def generateOutput(self, criteriaObject):
        return False

    
