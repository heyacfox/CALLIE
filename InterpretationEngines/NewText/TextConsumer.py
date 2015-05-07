#Text consumer, a consumer which takes in anything that's a string
from .. import Consumer
from .. import PartMachine
from .. import Constants
from .. import AnyPart
from .. import Connections
from .. import CallieMachine
from .. import Errors


class TextConsumer(Consumer.Consumer):
    mergeDataLimit = 20
    partMachine = ""

    def __init__(self, newData, newPartMachine):
        self.partMachine = newPartMachine
        self.data = newData

    #this is the one publicly okay
    def addDataToMachine(self):
        mydata = self.data
        print(str(self.partMachine.LossLimit))
        myPartMachine = self.partMachine
        self.beginConsume(mydata, myPartMachine)
        return myPartMachine


    #Okay, I don't handle OutOfMemoryErrors, but I DO handle NotInMemoryErrors
    #Those things are my triggers to add something to the database
    #ASSUME THE DATA IS A TEXT STRING. IF NOT TEXT I DUNNO
    def beginConsume(self, data, partMachine):
        startString = data[0]
        remainingData = data[1:]
        self.ensureBlankInMachine(partMachine)
        #myq = self.consumeNextPart("", startString, remainingData, partMachine)
        myremainingData = self.consumeNextPart("", startString, remainingData, partMachine)
        #print(myremainingData)
        #print("Top Data=" + myq)
        #we started the thing
        #maybe I should be running a while loop here, with the consumeNExtPart
        #returning the remaining data to use
        while len(myremainingData) > 1:
            #we must have at least 2 things left to get here, since we get back a remaining data greater than 0 and
            #a string part of some length
            myremainingData = self.consumeNextPart(myremainingData[0], myremainingData[1], myremainingData[2:], partMachine)
        print("We hit the end of the while loop")

    def consumeNextPart(self, previousPart, stringPart, remainingData, partMachine):
        try:
            print("Previous: " + previousPart + "|Next: " + stringPart)
            #At this point, what I'm really doing is trying to find the next string
            #regardless of what happens, we add connections to the previous part at the end
            stringDataPart = partMachine.getPartByID(stringPart)
            #if the combo of this thing and next thing is a connection we have
            #we should go to that instead
            if len(remainingData) > 0:
                #check to see if we have a connection to the next thing in a merge
                if stringDataPart.hasConnectionHuhInType(stringPart + remainingData[0], "Next"):
                    #We totaly have that connection! Run this function recursively with that merge, since we
                    #want to use the biggest value possible
                    print("Going Down a level after connection to deeper part found")
                    return self.consumeNextPart(previousPart, stringPart + remainingData[0], remainingData[1:], partMachine)
                else:
                    #We don't have that connection, but we need to determine if we should
                    #be creating a merge right now
                    if stringDataPart.hasConnectionHuhInType(remainingData[0], "Next"):
                        oldConnection = stringDataPart.getConnectionInType(remainingData[0], "Next")
                        #if we've hit the merge Data limit, we should create a new merge
                        print("Weight of Connection: " + str(oldConnection.weight))
                        if oldConnection.weight >= self.mergeDataLimit:
                            print("Passing part to Merge Create: " + stringPart + remainingData[0])
                            partMachine.receiveNewPart(stringPart + remainingData[0], stringPart + remainingData[0], Constants.conTypesForText)
                            print("Going down a level after merge")
                            return self.consumeNextPart(previousPart, stringPart + remainingData[0], remainingData[1:], partMachine)
                        else:
                            #This function will just make sure that we write the connections to each other
                            self.connectParts(previousPart, stringPart, partMachine)
                            #We return the remaining data to the above
                            print("TopConnect")
                            return (stringPart + remainingData)
                    else:
                        #if we hit this, then we don't have a deeper connection to the next thing.
                        self.connectParts(previousPart, stringPart, partMachine)
                        #print("X")#if we don't have a connection to the next thing, IGNORE
                        print("BottomConnect")
                        #print(stringPart + "|" + remainingData)
                        y = (stringPart + remainingData)
                        #print(y)
                        #z = len(y)
                        #print(z)
                        return y
                        print("did you actually return")
            else:
                #if we don't have any more things in the remaining data THis is it we're done write the connections and
                #stop the recursion
                self.connectParts(previousPart, stringPart, partMachine)
                print("LastConnect")
                return ""
        except Errors.NotInMemoryError:
            #we if our string part doesn't exist, we need to add it to memory before we do anything else.
            partMachine.receiveNewPart(stringPart, stringPart, Constants.conTypesForText)
            print("Added new part: " + stringPart)
            #Then we just run the function again. It won't crash this time.
            return self.consumeNextPart(previousPart, stringPart, remainingData, partMachine)
            print("sure we ran the check")
        raise RuntimeError("How did you even get here")

    def connectParts(self, previousPart, stringPart, partMachine):
        stringDataPart = partMachine.getPartByID(stringPart)
        previousDataPart = partMachine.getPartByID(previousPart)
        previousDataPart.addConnection("Next", Connections.Connection("TextCallieMachine", stringPart))   
        stringDataPart.addConnection("Previous", Connections.Connection("TextCallieMachine", previousPart))
        print("Connection:|" + previousPart + "| -> |" + stringPart + "||Weight: " + str(previousDataPart.getConnectionInType(stringPart, "Next").weight))

    def ensureBlankInMachine(self, partMachine):
        try:
            blankDataPart = partMachine.getPartByID("")
            print("placed it in machine")
        except Errors.NotInMemoryError:
            print("Not in machine yet")
            partMachine.receiveNewPart("", "", Constants.conTypesForText)
            
               
        """except Errors.NotInMemoryError:
            print("Receiving New Part: " + stringPart)
            partMachine.receiveNewPart(stringPart, stringPart, Constants.conTypesForText)
            stringDataPart = partMachine.getPartByID(stringPart)
        if outsideTrigger == 1:
            try:
                previousDataPart = partMachine.getPartByID(previousPart)
            except Errors.NotInMemoryError:
                #If the previous part doesn't exist, we can't add a connection to it. So Create it and add the connection
                partMachine.receiveNewPart(previousPart, previousPart, Constants.conTypesForText)
                previousDataPart = partMachine.getPartByID(previousPart)
            previousDataPart.addConnection("Next", Connections.Connection("TextCallieMachine", stringPart))   
            stringDataPart.addConnection("Previous", Connections.Connection("TextCallieMachine", previousPart))
            print("Connection:|" + previousPart + "| -> |" + stringPart + "|")
            print("Weight of Pushed Connection: " + str(previousDataPart.getConnectionInType(stringPart, "Next").weight))
            if len(remainingData) > 0:
                self.consumeNextPart(stringPart, remainingData[0], remainingData[1:], partMachine)
            else:
                #There is no more data. We cannot progress any further
                print("ConcludedConsuming")
            """



    #How do we decide whether or not to merge a connection
