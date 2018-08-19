from .. import Generator
import os


class SimpleGenerator(Generator.Generator):
    partMachine = ""

    def __init__(self, newPartMachine, totalRows):
        self.totalRows = totalRows
        self.partMachine = newPartMachine

    def generate(self):
        listOfResults = []
        seereturn = []
        for x in range(0, self.totalRows):
            listOfResults.append("bro")
        seereturn.append(listOfResults)
        seereturn.append(listOfResults)
        return seereturn

    #Takes in a list of things and saves it to a new file in the folder
    def saveIt(self):
        pass

        
