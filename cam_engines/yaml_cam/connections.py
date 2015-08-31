#The connections class. Handles connections between parts

class ConnectionTypeList:
    type_id = ""
    list_of_connection = {}

    def __init__(self, new_type_id):
        self.type_id = new_type_id
        self.list_of_connection = {}

    def add_type_connection(self, new_connection):
        self.list_of_connection[new_connection.part_id] = new_connection

    def pretty_print(self):
        print("Pretty Print Initalized for ConnectionTypeList: " + self.type_id)
        for key in self.list_of_connection.keys():
            print("Key: " + key + "|Weight: " + str(self.list_of_connection[key].weight))
            
    

#Why the eff do connections need to access the Callie Machine? They are WAY too
#low level to even BEGIN touching something like that. 
class Connection:
    callie_machine_str_ref = ""
    part_id = ""
    weight = 1

    def __init__(self, new_callie_machine_id, new_part_id):
        self.callie_machine_str_ref = new_callie_machine_id
        self.part_id = new_part_id
        self.weight = 1

    def add_weight(self, value):
        self.weight = self.weight + value
    
