from InterpretationEngines import callie_machine
#import CallieMachine
from InterpretationEngines.char_reader import char_consumer
from InterpretationEngines.char_reader import char_generator
from InterpretationEngines.images import pixel_consumer
from InterpretationEngines.images import pixel_generator
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

NEW_CALLIE = callie_machine.CallieMachine('pixel_storage.yaml', 'pixel_machine')
"""
for x in range(0, 30):
    for filename in os.listdir(os.getcwd() + "\\TopDataStore"):
        NEW_CALLIE.consume_content(pixel_consumer.PixelConsumer(Image.open('TopDataStore/' + filename), NEW_CALLIE.data_storage_class))
 """   
NEW_CALLIE.generate_output(pixel_generator.PixelGenerator(NEW_CALLIE.data_storage_class, 100, 100, tuple([1, 1])))
