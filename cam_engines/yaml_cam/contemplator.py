#This class will consume some type of data and stick it in a PartMachine

class Contemplator:
    data = ""
    part_machine = ""

    def __init__(self, new_data, new_part_machine):
        self.data = new_data
        self.part_machine = new_part_machine

    def add_data_to_machine(self):
        #this must return a part machine, it may be altered in some way
        #or it might not or whatever. The individual consumer gets to
        #decide this
        #generically, just return the machine
        return self.part_machine

    
