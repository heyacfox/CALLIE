#THis is the CallieMachine Class. All other CallieMachines must
#inherit from this design

import yaml
from . import PartMachine
from . import Constants
from . import Errors

class CallieMachine:
    callieMachineID = ""
    dataStorageLocation = ""
    dataStorageClass = ""



    def __init__(self, newDataStorageLocation, newID):
        self.dataStorageLocation = newDataStorageLocation
        #creates the file if it does not exist
        try:
            with open(newDataStorageLocation) as file:
                file.close()
        except IOError as e:
            self.createStorageLocation()
        self.dataStorageClass = self.returnClassFromData()
        self.callieMachineID = newID

    #this must be implemented on every machine
    def returnClassFromData(self):
        stream = open(self.dataStorageLocation)
        print("Imported Class")
        return yaml.load(stream)
        

    #this is called when the thing is created. This is
    #how we get a starter file to work with
    def saveClassToData(self):
        stream = open(self.dataStorageLocation, 'w')
        yaml.dump(self.dataStorageClass, stream)
        stream.close()
        print("Saved Class")

    def consumeContent(self, newConsumer):
        try:
            dataMachineToSave = newConsumer.addDataToMachine()
            self.dataStorageClass = dataMachineToSave
            self.saveClassToData()
            print("Consumed Data and saved")
        except Errors.OutOfMemoryError:
            self.dataStorageClass.initiateLossyMemoryExpansion()
            print("Ran Memory Adjustment")

    def generateOutput(self, newGenerator):
        return newGenerator.generate()
        print("Generated Output")

    def createStorageLocation(self):
        stream = open(self.dataStorageLocation, 'w')
        yaml.dump(PartMachine.PartMachine(Constants.myLossLimit, Constants.myExpansionMax), stream)
        stream.close()
        print("Created Storage Location")
