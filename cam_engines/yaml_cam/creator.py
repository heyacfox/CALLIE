#This class takes a PartMachine and can do whatever it wants with it. Returns some output

class Generator:
    part_machine = ""

    def __init__(self, new_part_machine):
        self.part_machine = new_part_machine

    def create(self):
        #implement this in subclasses. Returning a blank string is
        #a perfectly legit output for this Maybe you wanna do something
        #more useful though
        return ""
