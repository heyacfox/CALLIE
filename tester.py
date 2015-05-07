from InterpretationEngines import CallieMachine
#import CallieMachine
from InterpretationEngines.NewText import TextConsumer
from InterpretationEngines.NewText import TextGenerator
import yaml

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
