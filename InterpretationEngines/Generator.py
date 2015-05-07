#This class takes a PartMachine and can do whatever it wants with it.

class Generator:
    partMachine = ""

    def __init__(self, newPartMachine):
        self.partMachine = newPartMachine

    def generate(self):
        #implement this in subclasses. Returning a blank string is
        #a perfectly legit output for this
        return ""
