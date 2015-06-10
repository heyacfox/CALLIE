#Part Class
from . import constants
import random

class AnyPart:
    part_id = ""
    part_value = ""
    list_of_connection_types = {}
    
    def __init__(self, my_id, my_value, dictionary_of_con_types):
        self.part_id = my_id
        self.part_value = my_value
        self.list_of_connection_types = dictionary_of_con_types

    def add_connection(self, type_list_id, new_connection):
        if type_list_id in self.list_of_connection_types:
            if new_connection.part_id in self.list_of_connection_types[type_list_id].list_of_connection:
                #print("Anypart: Added Weight")
                self.list_of_connection_types[type_list_id].list_of_connection[new_connection.part_id].add_weight(constants.WEIGHT_TO_ADD)
            else:
                #print("Anypart: Made new connection")
                self.list_of_connection_types[type_list_id].add_type_connection(new_connection)
        else:
            raise RuntimeError('Not in types')

    def return_random_connection(self):
        new_dictionary = random.choice(list(self.list_of_connection_types.keys()))
        new_connection = random.choice(list(new_dictionary.keys()))
        return new_connection

    def return_random_connection_in_type(self, type_search_id):
        new_connection = random.choice(self.list_of_connection_types[type_search_id].keys())
        return newConnection

    def return_weighted_random_connection_in_type(self, type_search_id):
        totally_new_dictionary = self.list_of_connection_types[type_search_id].copy()
        totalWeight = 0
        for key, value in totally_new_dictionary:
            total_weight = total_weight + value.weight
        #after we have generated our total connection weights, we can do the breakdown
        random_weight = random.randint(1, total_weight - 1)
        for key, value in totally_new_dictionary:
            random_weight = random_weight - value.weight
            if random_weight < 0:
                return value

    def return_total_connection_weight(self):
        total_connections_and_weights = 0
        for x in self.list_of_connection_types.values():
            for y in x.values():
                total_connections_and_weights = total_connections_and_weights + y.weight
        return total_connections_and_weights


    def has_connection(self, some_part_id):
        #This should be checking to see if there is a connection in ANY of my types
        raise RuntimeError()


    def has_connection_in_type(self, some_part_id, some_type):
        if some_type in self.list_of_connection_types:
            if some_part_id in self.list_of_connection_types[some_type].list_of_connection:
                return True
        return False

    def get_connection_in_type(self, some_part_id, some_type):
        return self.ListOfConnectionTypes[someType].listOfConnection[somePartID]

    #returns ALL CONNECTION KEYS MAKE SURE YOU WANT THIS
    def get_all_connections_in_type(self, some_type):
        return self.list_of_connection_types[some_type].keys()

    def pretty_print(self):
        print(self.part_value)
