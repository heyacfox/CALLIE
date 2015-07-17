from .. import generator
from .. import part_machine
from .. import connections
from .. import any_part
from .. import errors
from .. import constants

class CharGenerator:

    def __init__(self, new_part_machine, text_length):
        self.part_machine = new_part_machine
        self.text_length = text_length

    def generate(self):
        #first, get a part
        #Then, get a connection from that part.
        #IF A PART HAS NO CONNECTIONS, WE GET AN ERROR BACK
        #THIS NEEDS TO BE A TRY-EXCEPT
        #OR JUST USE THE has_any_connections function
        starter_part = self.part_machine.get_part_by_id(self.part_machine.get_any_part_id())
        i = 0
        list_of_part_ids = [None] * (self.text_length)
        list_of_part_ids[i] = starter_part.part_id
        i = i + 1
        cur_part = starter_part
        while i < self.text_length:
            
            #This will do this step text_legth number of steps
            #IF WE CAN'T FIND ANY CONNECTION, WE NEED TO GO BACK A LEVEL.
            #IF WE GO BACK TO 0 THEN SO BE IT
            #If i goes back to zero, we have to get a random part again
            if cur_part.has_any_connection:
                #WE ARE ALREADY AT THE CORRECT i RIGHT NOW
                new_connection = cur_part.return_weighted_random_connection_in_type("Next")
                list_of_part_ids[i] = new_connection.part_id
                cur_part = self.part_machine.get_part_by_id(new_connection.part_id)
                #ITERATION HAPPENS AT THE END
                i = i + 1
            else:
                #This part is hopeless. Go back a level
                if i == 0:
                    #IF I IS EQUAL TO ZERO, GET A RANDOM PART AND START AGAIN
                    cur_part = self.part_machine.get_part_by_id(self.part_machine.get_any_part_id())
                    list_of_part_ids[i] = cur_part.part_id
                    i = i + 1
                else:
                    #OTHERWISE, get the previous part in the index
                    i = i - 1
                    previous_id_to_use = list_of_part_ids[i]
                    cur_part = self.part_machine.get_part_by_id(previous_id_to_use)
                    
        #ONCE WE ARE OUT OF THE WHILE
        return_string = ""
        for x in list_of_part_ids:
            return_string = return_string + self.part_machine.get_part_by_id(x).part_value
        return return_string
        #AT THE END, CONVERT ALL IDs TO VALUES
            
        
