from .. import consumer
from .. import part_machine
from .. import connections
from .. import any_part
from .. import errors
from .. import constants
import copy

global TALK_EVERY
TALK_EVERY = 2000


class CharConsumer(consumer.Consumer):


    def add_data_to_machine(self):
        new_machine = self.begin_consume(self.data, self.part_machine)
        return new_machine

    def begin_consume(self, data, part_machine_obj):
        recycle_data = data
        talk_value = 0
        global TALK_EVERY
        while len(recycle_data) > 2:
            self.consume_char(recycle_data[0], recycle_data[1], part_machine_obj)
            recycle_data = recycle_data[1:]
            if (talk_value >= TALK_EVERY):
                talk_value = 0
                print("Chars Remaining: " + str(len(recycle_data)))
            else:
                talk_value = talk_value + 1
        #YOU GOTTA CALL THE FINAL CONNECTION BEFORE RETUNING MUST BE OBJECTS
        return part_machine_obj

    def consume_char(self, this_char, next_char, part_machine_obj):
        #passing in the 5th and 6th values are important if we need to make a new any_part
        #If you're SURE we don't need to make a new one, we don't have to pass those in
        #print("Consuming char: |" + this_char + "| next is |" + next_char + "|")
        part_machine_obj.add_connection_to_part(this_char,
                                                "Next",
                                                "Self",
                                                next_char,
                                                this_char,
                                                copy.deepcopy(constants.CON_TYPES_FOR_TEXT))
