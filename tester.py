from InterpretationEngines import callie_machine
#import CallieMachine
from InterpretationEngines.char_reader import char_consumer
from InterpretationEngines.char_reader import char_generator
#from InterpretationEngines.char_reader import TextGenerator
import yaml
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

NEW_CALLIE = callie_machine.CallieMachine('char_storage.yaml', 'char_machine')
#NEW_CALLIE.consume_content(char_consumer.CharConsumer(open("mobydick.txt").read(), NEW_CALLIE.data_storage_class))
print("OUTPUT:" + NEW_CALLIE.generate_output(char_generator.CharGenerator(NEW_CALLIE.data_storage_class, 1000)))
