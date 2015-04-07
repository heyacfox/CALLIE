#! usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from random import randint
import TextPartClass
import XMLGetterSetter

#constants
global DepthCallAmount
DepthCallAmount = 20
global PrintOnNumber
PrintOnNumber = 400

#Variables
global SavedState
SavedState = ""
global SavedPart
global GlobalTopTextPart
global PrintOnNumberCounter
PrintOnNumberCounter = 0

##----
#Public Functions

#Returns a built text file
def writeTextStory(textpath, chars, CM):
    MyTextPart = XMLGetterSetter.getXMLReturnTP(CM)
    #openText returns a text file.
    MyTextFile = openText(textpath)
    StoryString = writeStory(MyTextPart, chars)
    writeStringToText(StoryString, MyTextFile)
    MyTextFile.close()
    
#Returns a string
def writeString(chars, CM):
    MyTextPart = XMLGetterSetter.getXMLReturnTP(CM)
    return writeStory(MyTextPart, chars)
    
#---------


def openText(path):
    return open(path, 'w')

def writeStory(textpart, chars):
    from random import randint
    indexesOfNext = len(textpart.NextElements)
    someIndex = randint(0, indexesOfNext)
    global SavedPart
    global SavedState
    buildstring = ""
    #the mypart cycles down to the lowest state we got
    mypart = findPartAtDepths(textpart)
    CharsLeft = chars
    SavedState = mypart.ThisElement
    #print("SavedState:" + SavedState)
    writeOneThing(mypart.ThisElement, buildstring)
    CharsLeft = CharsLeft - len(SavedState)
    while CharsLeft > 1:
        #print("Chars Left: " + str(CharsLeft))
        buildstring = writeRandomOutcome(mypart, buildstring)
        CharsLeft = CharsLeft - len(SavedState)
        #print("WroteOutcome:" + SavedState)
        mypart = findPartAtDepths(findPart(SavedState, textpart))
        printEveryNumber(len(SavedState), CharsLeft)
        #print("SavedState: " + SavedState + "| and mypart: " + mypart.ThisElement)
    return buildstring

def printEveryNumber(incrementer, charsleft):
    global PrintOnNumber
    global PrintOnNumberCounter
    if PrintOnNumberCounter > PrintOnNumber:
        PrintOnNumberCounter = 0
        print(str(charsleft))
    else:
        PrintOnNumberCounter = PrintOnNumberCounter + incrementer

def writeStoryRecur(part, buildstring):
    from random import randint
    indexofOutcomes = len(part.Outcomes)
    someIndex = randint(0, indexofOutcomes-1)
    myoutcome = part.Outcomes[someIndex].Value
    return writeOneThing(myoutcome, buildstring)
    global SavedState
    SavedState = myoutcome

#returns the altered buildstring, alters the savedState
def writeRandomOutcome(part, buildstring):
    from random import randint
    TotalOutcomesSize = 0
    for outcome in part.Outcomes:
        TotalOutcomesSize = TotalOutcomesSize + outcome.TimesCalled
    #print("OutcomeSizeCheck:"+str(TotalOutcomesSize))
    someindex = randint(0, TotalOutcomesSize)
    for outcome in part.Outcomes:
        #print("OutcomeSizeCheck:"+str(TotalOutcomesSize))
        if TotalOutcomesSize <= 1:
            global SavedState
            SavedState = outcome.Value
            return writeOneThing(outcome.Value, buildstring)
        else:
            TotalOutcomesSize = TotalOutcomesSize - outcome.TimesCalled
    #print("I should never be here")
    
    

#We ALWAYS try to go as far down as we can before we get an outcome
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


def writeOneThing(thing, buildstring):
    buildstring = buildstring + str(thing)
    #print("Wrote: " + thing)
    return buildstring

def findPart(somestate, mytoptextpart):
    return findPartHelp(somestate, somestate, mytoptextpart, 0)

def findPartHelp(somestate, fullstate, part, indexcheck):
    if fullstate == part.ThisElement:
        return part
    else:
        for ele in part.NextElements:
            if somestate[0] == ele.ThisElement[indexcheck]:
                return findPartHelp(somestate[1:], fullstate, ele, indexcheck + 1)
    print("No Part Found")

#Returns a string

def writeSomeText(CM, mychars):
    getXML(CM)
    openText("tweettemplate.txt")
    writeStory(mychars)
    global TextFile
    saveText()
    newTextFile = open("tweettemplate.txt", 'r')
    SomeTweet = newTextFile.read()
    return SomeTweet
