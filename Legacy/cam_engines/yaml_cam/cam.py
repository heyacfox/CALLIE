#THis is the CallieMachine Class. All other CallieMachines must
#inherit from this design

import yaml
from . import part_machine
from . import constants
from . import errors

class CAM:
    CAM_id = ""
    data_storage_location = ""
    data_storage_class = ""



    def __init__(self, new_data_storage_location, new_id):
        self.data_storage_location = new_data_storage_location
        #creates the file if it does not exist
        try:
            with open(new_data_storage_location) as file:
                file.close()
        except IOError as e:
            print("No file here yet, creating new file")
            self.create_storage_location()
        self.data_storage_class = self.return_class_from_data()
        self.CAM_id = new_id

    #this must be implemented on every machine
    def return_class_from_data(self):
        stream = open(self.data_storage_location)
        print("Imported Class")
        return yaml.load(stream)
        

    #this is called when the thing is created. This is
    #how we get a starter file to work with
    def save_class_to_data(self):
        stream = open(self.data_storage_location, 'w')
        yaml.dump(self.data_storage_class, stream)
        stream.close()
        print("Saved Class")

    def contemplate_content(self, new_contemplator):
        try:
            data_machine_to_save = new_contemplator.add_data_to_machine()
            self.data_storage_class = data_machine_to_save
            self.save_class_to_data()
            print("Consumed Data and saved")
        except errors.OutOfMemoryError:
            self.data_storage_class.initiate_lossy_memory_expansion()
            print("Ran Memory Adjustment")

    def create_content(self, new_creator):
        return new_creator.create()
        print("Generated Output")

    def create_storage_location(self):
        stream = open(self.data_storage_location, 'w')
        yaml.dump(part_machine.PartMachine(constants.MY_LOSS_LIMIT, constants.MY_EXPANSION_MAX), stream)
        stream.close()
        print("Created Storage Location")
