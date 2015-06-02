from .. import Consumer
from .. import Errors
from .. import Connections
import copy

import csv
global conTypeSimple
conTypeSimple = Connections.ConnectionTypeList("Simple")
conTypeExternal = Connections.ConnectionTypeList("External")

global allMyConTypes
allMyConTypes = {conTypeSimple.typeID: copy.deepcopy(conTypeSimple), conTypeExternal.typeID: copy.deepcopy(conTypeExternal)}


class simpleConsumer(Consumer.Consumer):
    data = ""
    partMachine = ""

    def addDataToMachine(self):
        #print("adding")
        someFileOpened = open(self.data, "r")
        reader = csv.reader(someFileOpened)
        for row in reader:
            #a row is a list of two elements. We want to make connections from
            #one to another
            #print(row)
            self.addOneConnection(row)
        return self.partMachine

    def addOneConnection(self, oneRow):
        firstPart = oneRow[0]
        secondPart = oneRow[1]
        try:
            thePart = self.partMachine.getPartByID(firstPart)
            thePart.addConnection("Simple", Connections.Connection("Simple", secondPart))
        except Errors.NotInMemoryError:
            #if we don't have the part
            global conTypes
            self.partMachine.receiveNewPart(firstPart, firstPart, copy.deepcopy(allMyConTypes))
