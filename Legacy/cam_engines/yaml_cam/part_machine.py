from . import errors
from . import any_part
import math
import random
from . import connections

#This is the dataStorageClass

class PartMachine:
    #Parts is a dictionary, because there is an ID for everything I need.
    #The connections are handled internally after the part is retrieved
    list_of_parts = {}
    loss_limit = 0
    max_expansion_percentage = 0.0

    def __init__(self, start_loss_limit, start_expansion_percentage):
        self.loss_limit = start_loss_limit
        self.max_expansion_percentage = start_expansion_percentage
        #So here's something crazy. PartMachine DOES NOT
        #INITIALIZE WITH LIST OF PARTS EVER
        #It is always handled on the outside.
        self.list_of_parts = {}

    #a public function that will return a part from the list based 
    def get_part_by_id(self, search_id):
        if search_id in self.list_of_parts:
            return self.list_of_parts[search_id]
        else:
            raise errors.NotInMemoryError(search_id)

    def receive_new_part(self, new_part_id, new_part_value, dict_of_con_types):
        if len(self.list_of_parts) >= self.loss_limit:
            #We stop the consuming, we cannot handle anything more
            raise OutOfMemoryError()
        else:
            if new_part_id in self.list_of_parts:
                raise RuntimeError("Part Already Exists")
            else:
                self.list_of_parts[new_part_id] = any_part.AnyPart(new_part_id, new_part_value, dict_of_con_types)

    def initiate_lossy_memory_expansion(self):
        #create a list fro the listOfParts dictionary
        new_list = self.list_of_parts.values()
        #Sort the list by the amount of connections the parts have
        new_list.sort(key=lambda x: x.return_total_connection_weight(), reverse=True)
        #remove MaxExpansionPercentage % of the list, record that number
        number_to_remove = math.floor(float(self.loss_limit) * self.max_expansion_percentage)
        list_to_remove = new_list[:(number_to_remove - 1)]
        for x in list_to_remove:
            removed = self.list_of_parts.pop(x.part_id)
        #Add that number to the LossLimit
        self.loss_limit = self.loss_limit + number_to_remove
        return "X"

    def get_any_part_id(self):
        some_part_id = random.choice(list(self.list_of_parts.keys()))
        return some_part_id

    def pretty_print(self):
        "PartMachine Pretty Print Initializing..."
        for key in self.list_of_parts.keys():
            print("Key:" + key)
            list_of_parts[key].pretty_print()
            
    def has_part(self, part_id):
        if part_id in self.list_of_parts.keys():
            return True
        else:
            return False

    def add_connection_to_part(self, from_part_id, connection_type_id, to_callie_machine, to_part_id, passed_value=0, passed_connection_list=[]):
#       #If we already have the part, we add a connection to it
        if self.has_part(from_part_id):
            part_obj_to_alter = self.get_part_by_id(from_part_id)
            new_connection = connections.Connection(to_callie_machine, to_part_id)
            part_obj_to_alter.add_connection(connection_type_id, new_connection)
        #If we do not have the part, add it then add connection
        else:
            #I don't like where this is going.
            self.receive_new_part(from_part_id, passed_value, passed_connection_list)
            part_obj_to_alter = self.get_part_by_id(from_part_id)
            new_connection = connections.Connection(to_callie_machine, to_part_id)
            part_obj_to_alter.add_connection(connection_type_id, new_connection)
