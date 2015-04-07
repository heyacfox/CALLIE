#! usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from random import randint
#The class for defining a part of a text
class TextPart:
    ThisElement = ""
    TimesCalled = 0
    NextElements = []
    Outcomes = []

    def __init__(self, thisElement):
        self.ThisElement = thisElement
        self.TimesCalled = 1
        self.NextElements = []
        self.Outcomes = []

class Outcome:
    Value = ""
    TimesCalled = 0

    def __init__(self, somevalue):
        self.Value = somevalue
        self.TimesCalled = 1
global DepthCallAmount
DepthCallAmount = 5
global TopTextPart
global TextFile
global CharsLeft
global SavedState
global SavedPart
TopTextPart = TextPart("")


def getXML(path):
    tree = ET.parse(path)
    root = tree.getroot()
    TopTextPart.TimesCalled = int(root[0][1].text)
    #print(str(TopTextPart.TimesCalled))
    #print("Root: " + root[1].text)
    populateTreeForPart(TopTextPart, root[0])
    


def populateTreeForPart(part, element):
    for nextpart in element[2]:
        #print("AddingPart: " + str(nextpart[0].text))
        newpart = TextPart(nextpart[0].text)
        newpart.TimesCalled = int(nextpart[1].text)
        for potoutcome in nextpart[3]:
            newoutcome = Outcome(potoutcome[0].text)
            newoutcome.TimesCalled = int(potoutcome[1].text)
            newpart.Outcomes.append(newoutcome)
        part.NextElements.append(newpart)
        #newpart.NextElements = []
        #newpart.Outcomes = []
        #print("New Part: " + str(newpart.ThisElement) + " " + str(newpart))
        #print("Old Part: " + str(part.ThisElement) + " " + str(part))
        populateTreeForPart(newpart, nextpart)

def openText(path):
    global TextFile
    TextFile = open(path, 'w')

def saveText():
    global TextFile
    TextFile.close()

def writeStory(chars):
    global TextFile
    global TopTextPart
    from random import randint
    indexesOfNext = len(TopTextPart.NextElements)
    someIndex = randint(0, indexesOfNext)
    global CharsLeft
    global SavedPart
    global SavedState
    mypart = findPartAtDepths(TopTextPart)
    #mypart = TopTextPart.NextElements[someIndex]
    CharsLeft = chars
    writeOneThing(mypart.ThisElement)
    while CharsLeft > 1:
        print("Chars Left: " + str(CharsLeft))
        writeStoryRecur(mypart)
        mypart = findPartAtDepths(findPart(SavedState))
        print("SavedState: " + SavedState + "| and mypart: " + mypart.ThisElement)
        newStateAdditionalslice = slice(len(SavedState), len(mypart.ThisElement))
        writeOneThing(mypart.ThisElement[newStateAdditionalslice])
        
def writeStoryRecur(part):
    from random import randint
    #if (part is None):
    #    part = selectNewRandomPart()
    indexofOutcomes = len(part.Outcomes)
    someIndex = randint(0, indexofOutcomes-1)
    #if len(part.Outcomes) == 0:
    #    print("WHY ARE THERE NO OUTCOMES FOR: " + part.ThisElement)
    myoutcome = part.Outcomes[someIndex].Value
    writeOneThing(myoutcome)
    global SavedState
    SavedState = myoutcome

def findPartAtDepths(part):
    global DepthCallAmount
    #print(str(part.TimesCalled))
    if part.NextElements == []:
        return part
    if part.TimesCalled < DepthCallAmount:
        return part
    else:
        #print("Entering Recursion Loop")
        return findPartAtDepths(findNextPartAtXAway(part))
    

def findNextPartAtXAway(part):
    #print("Next Part at index: " + str(part.TimesCalled))
    dist = randint(0, part.TimesCalled)
    #print(str(dist))
    #print(str(part.NextElements))
    if(part.NextElements == []):
        return part
    for sp in part.NextElements:
        if dist <= 5:
            #print(str(sp))
            return sp
        else:
            dist = dist - sp.TimesCalled
            #print(str(dist))
    #If we fail all these, just return the first element
    return part.NextElements[0]


def writeOneThing(thing):
    global TextFile
    global CharsLeft
    CharsLeft = CharsLeft - len(thing)
    TextFile.write(thing)
    print("Wrote: " + thing)

def selectNewRandomPart():
    global TopTextPart
    from random import randint
    indexesOfNext = len(TopTextPart.NextElements)
    someIndex = randint(0, indexesOfNext-1)
    global CharsLeft
    global SavedPart
    global SavedState
    mypart = TopTextPart.NextElements[someIndex]
    return mypart

#this will return a part, based on the state
def findPart(somestate):
    global TopTextPart
    #print("FullState: " + somestate)
    return findPartHelp(somestate, somestate, TopTextPart, 0)

def findPartHelp(somestate, fullstate, part, indexcheck):
    if fullstate == part.ThisElement:
        return part
    else:
        #print("Part was: " + part.ThisElement)
        #print("Somestate[0]: " + somestate[0])
        for ele in part.NextElements:
            if somestate[0] == ele.ThisElement[indexcheck]:
                return findPartHelp(somestate[1:], fullstate, ele, indexcheck + 1)
    print("No Part Found")

def main():
    print("Start")
    getXML("CALLIEMachine.xml")
    print("XML Retrieved, opening file.")
    openText("teststory.txt")
    print("Writing Story")
    writeStory(3000)
    print("Closing Files")
    saveText()
    print("Complete")
    
main()
