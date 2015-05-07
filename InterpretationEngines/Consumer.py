#This class will consume some type of data and stick it in a PartMachine

class Consumer:
    data = ""
    partMachine = ""

    def __init__(self, newData, newPartMachine):
        self.data = newData
        self.partMachine = newPartMachine

    def addDataToMachine(self):
        #this must return a part machine, it may be altered in some way
        #or it might not or whatever. The individual consumer gets to
        #decide this
        #generically, just return the maachine
        return self.partMachine

    
