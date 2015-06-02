from InterpretationEngines.Simple import SimpleConsumer
from InterpretationEngines import PartMachine
from InterpretationEngines import CallieMachine
from InterpretationEngines.Simple import SimpleGenerator
import csv
import os

#takes a list of lists and saves it to a csv file
def saveListsToCSV(LoL, pathLocation):
        mypath = pathLocation
        num_files = len([f for f in os.listdir(mypath)if os.path.isfile(os.path.join(mypath, f))])
        print(str(num_files))
        actualName = pathLocation + "Generated" + str(num_files) + ".csv"
        resultFile = open(actualName, 'w', newline='')
        wr = csv.writer(resultFile, dialect='excel')
        print(LoL)
        wr.writerows(LoL)
    

simpleCallieMachine = CallieMachine.CallieMachine("here.yaml", "Simple")

simplePartMachine = PartMachine.PartMachine(1000000000, 2.0)

myNewSimple = SimpleConsumer.simpleConsumer("InterpretationEngines/Simple/ReadingData/Links.csv", simplePartMachine)
"""
myNewSimple.addDataToMachine()
"""

myNewSimpleGenerator = SimpleGenerator.SimpleGenerator(simplePartMachine, 5)
"""
outcome = myNewSimpleGenerator.generate()
"""
simpleCallieMachine.consumeContent(myNewSimple)
p = simpleCallieMachine.generateOutput(myNewSimpleGenerator)

saveListsToCSV(p, "InterpretationEngines/Simple/GeneratedData/")

simpleCallieMachine.saveClassToData()


#Bug Log:
#1. YAML doesn't save all of the part machine class, just the easy to save things. (MY BEAUTIFUL PARTMACHINE)
#2. SimpleGenerator doesn't generate based on the part machine yet.
#3. 


#print(outcome)
