from cam_engines.yaml_cam import cam
#import CallieMachine
#from content_engines.chars import char_contemplator
#from content_engines.chars import char_creator
from content_engines.images import pixel_contemplator
from content_engines.images import pixel_creator
#from InterpretationEngines.char_reader import TextGenerator
import yaml
from PIL import Image
import os
"""
class SomeClass():
    x = '5'
    y = '9'

    def __init__(self, myy):
        self.x = '6'
        self.y = myy

#yaml.dump(SomeClass('Zero'), open('someYAML.yaml', 'w'))

#loaded = yaml.load(open('someYAML.yaml', 'r'))
#print(loaded.x)
#print(loaded.y)

mynewCallie = CallieMachine.CallieMachine('tempyaml.yaml', 'testMachine')

print(str(mynewCallie.dataStorageClass.LossLimit))

mynewCallie.consumeContent(TextConsumer.TextConsumer(open("wolf2.txt").read(), mynewCallie.dataStorageClass))
"""

#NEW_CALLIE = callie_machine.CallieMachine('char_storage.yaml', 'char_machine')
#NEW_CALLIE.consume_content(char_consumer.CharConsumer(open("mobydick.txt").read(), NEW_CALLIE.data_storage_class))
#print("OUTPUT:" + NEW_CALLIE.generate_output(char_generator.CharGenerator(NEW_CALLIE.data_storage_class, 1000)))

NEW_CALLIE = cam.CAM('pixel_storage.yaml', 'pixel_machine')

for x in range(0, 1):
    for filename in os.listdir(os.getcwd() + "\\consumed_files\\png_images"):
        NEW_CALLIE.contemplate_content(pixel_contemplator.PixelContemplator(Image.open('consumed_files/png_images/' + filename), NEW_CALLIE.data_storage_class))
  
NEW_CALLIE.create_content(pixel_creator.PixelCreator(NEW_CALLIE.data_storage_class, 100, 100, tuple([1, 1])))
