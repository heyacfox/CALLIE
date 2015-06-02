from InterpretationEngines import CallieMachine
from InterpretationEngines.NewText import TextConsumer
from InterpretationEngines.NewText import TextGenerator
from InterpretationEngines import AnyPart
from InterpretationEngines import PartMachine
from InterpretationEngines import Connections

#-----Testing Class -----#
class Tester:
    testName = ""
    def __init__(self, newName, newCheck, newExpect):
        self.testName = newName
        self.Expect = newExpect
        self.Check = newCheck
        if self.Expect == self.Check:
            self.testResult = True
        else:
            self.testResult = False

def printAllFailedTestsInList(listOfTests):
    for test in listOfTests:
        if test.testResult == False:
            print("Name: " + test.testName + "\n"
                  + "  Check: " + test.Check + "\n"
                  + "  Expect: " + test.Expect)

def returnNumberOfFailedTests(listOfTests):
    returnvalue = 0
    for test in listOfTests:
        if test.testResult == False:
            returnvalue = returnvalue + 1
    return returnvalue

#-------Variables---------#
String1 = "He found a machine."
String2 = "1534-2||}{{{;;',./123!@#$%^&*()~`"
String3 = "Steve"

ConnectionTypeName1 = "SomeConnection"

AnyPartid1 = ""
AnyPartid2 = "n"
AnyPartid3 = "o"

CallieMachineName1 = "MyNewCM"

Connection1 = Connections.Connection(CallieMachineName1, AnyPartid2)
Connection2 = Connections.Connection(CallieMachineName1, AnyPartid3)

ConnectionTypeDictionary1 = {ConnectionTypeName1: {}}

AnyPart1 = AnyPart.AnyPart(AnyPartid1, AnyPartid1, ConnectionTypeDictionary1)
AnyPart2 = AnyPart.AnyPart(AnyPartid2, AnyPartid2, ConnectionTypeDictionary1)
AnyPart3 = AnyPart.AnyPart(AnyPartid3, AnyPartid3, ConnectionTypeDictionary1)

PartMachine1 = PartMachine.PartMachine(100, 0.2)




#-------Testers------------#


#PartMachine------------#
listOfPartMachineTests = []
CTD1 = ConnectionTypeDictionary1
PM1 = PartMachine1
AP1 = AnyPart1


PM1.receiveNewPart(AnyPartid2, AnyPartid2, CTD1)
PMTest1 = Tester("Receiving a Part and using getPartByID",
                 PM1.getPartByID(AnyPartid2).PartID,
                 AnyPartid2)
listOfPartMachineTests.append(PMTest1)

print("Part Machine Tests")                               
print(str(len(listOfPartMachineTests) - returnNumberOfFailedTests(listOfPartMachineTests)) + " out of " + str(len(listOfPartMachineTests)) + " tests passed.")
printAllFailedTestsInList(listOfPartMachineTests)



#-----AnyPart-------#
#This will test all functions in AnyPart
