#! usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os

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

global TopTextPart
TopTextPart = TextPart("")
global TextFile
global TextData
global TextDrain
global TimesRecurred
DepthTracker = 0
global DuplicateAmountDepth
DuplicateAmountDepth = 20
global CleanUpListTP
CleanUpListTP = []
global CleanUpListText
CleanUpListText = []


class Outcome:
    Value = ""
    TimesCalled = 0

    def __init__(self, somevalue):
        self.Value = somevalue
        self.TimesCalled = 1


# This prodecure will get the XML file and return
# A usable TextPart
def getXML(path):
    tree = ET.parse(path)
    root = tree.getroot()
    TopTextPart.TimesCalled = int(root[0][1].text)
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

#returns a collection of file paths for use in the openReadAllTxt function

#Opens all text files and reads all text files
def openReadAllTxt(textspaths):
    for filename in os.listdir(textspaths):
        openTxt(textspaths + "/" + filename)
        readTxtFile()

#opens the text file
def openTxt(path):
    #print("here")
    global TextData
    global TextFile
    TextFile = open (path, "r")
    TextData = TextFile.read()

#Closes the text file
def closeTxt():
    global TextFile
    TextFile.close()

#if a TextPart has NextElements, then the outcomes list for that
#should be removed, as it is not used
def cleanUnusedOutcomes():
    global TopTextPart
    cleanUnusedOutcomesRecursive(TopTextPart)

def cleanUnusedOutcomesRecursive(textpart):
    for tp in textpart.NextElements:
        if len(tp.NextElements) > 0:
            textpart.Outcomes = []
            cleanUnusedOutcomesRecursive(tp)

#this will check the length of the total thing
def removeOutcomesOfLength(someLength):
    #that length is a number value
    global TopTextPart
    removeOutcomesOfLengthRecursive(TopTextPart, someLength)

def removeOutcomesOfLengthRecursive(textpart, someLength):
    if len(textpart.NextElements) > 0:
        for oc in textpart.Outcomes:
            if len(oc) <= someLength:
                textpart.Outcomes.remove(oc)
    for tp in textpart.NextElements:
        removeOutcomesOfLengthRecursive(tp, someLength)

def reassignTimesCalled():
    global TopTextPart
    reassignTimesCalledRecursive(TopTextPart)

def reassignTimesCalledRecursive(textpart):
    global TopTextPart

#runs all the cleanup operations
def cleanData():
    cleanUnusedOutcomes()

#Saves the XML File out based on the whole TextParts
def saveXML(path):
    import xml.etree.cElementTree as NET
    global TopTextPart
    cleanData()
    root = NET.Element("root")
    TP = NET.SubElement(root, "TextPart")
    WritePartsRecursively(NET, TP, TopTextPart)
    tree = NET.ElementTree(root)
    tree.write(path)

def WritePartsRecursively(tree, part, partobject):
    #print("Value Printing: " + str(partobject.ThisElement))
    field1 = tree.SubElement(part, "ThisElement")
    field2 = tree.SubElement(part, "TimesCalled")
    field3 = tree.SubElement(part, "NextElements")
    field4 = tree.SubElement(part, "Outcomes")
    field1.text = str(partobject.ThisElement)
    field2.text = str(partobject.TimesCalled)
    for o in partobject.Outcomes:
        field41 = tree.SubElement(field4, "Outcome")
        field411 = tree.SubElement(field41, "Value")
        field411.text = str(o.Value)
        field412 = tree.SubElement(field41, "TimesCalled")
        field412.text = str(o.TimesCalled)
    for e in partobject.NextElements:
        field3e = tree.SubElement(field3, "TextPart")
        WritePartsRecursively(tree, field3e, e)
            
#reads through the file, adding to textpart as needed
def readTxtFile():
    #print("here")
    global TextData
    global TextDrain
    global SavedState
    TextDrain = TextData
    SavedState = TextDrain[0]
    TextDrain = TextDrain[1:]
    while len(TextDrain) > 1:
        #print(str(len(TextDrain)))
        print("New State Here: " + SavedState)
        stateRestCompare(SavedState, TextDrain)


#takes in a value and a long string, works through to decide
#how to add them to our TopTextPart
def stateRestCompare(state, rest):
    global TopTextPart
    global TextDrain
    #the state present here might have 1 or MORE characters
    if len(state) == 1:
        stateRestCompareRecursive(TopTextPart, state, rest)
    else:
        slic = slice(len(state)-1, len(TextDrain))
        stateRestCompareRecursive(findPart(state), state, rest)

def stateRestCompareRecursive(p, s, r):
    global TextDrain
    global DuplicateAmountDepth
    check = "false"
    if s == p.ThisElement:
        check = "Nocheck"
        if p.TimesCalled > DuplicateAmountDepth:
            news = s + TextDrain[0]
            TextDrain = TextDrain[1:]
            newr = TextDrain
            stateRestCompareRecursive(p, news, newr)
        else:
            findOutcomeForPart(p, s, r)
    #look through all next
    if check == "false":
        for stateelement in p.NextElements:
            #if this state is within the next elements
            #print("Usin g State: " + s + " |checking next of " + p.ThisElement)
            if s == stateelement.ThisElement:
                check = "true"
                #we have found a match. Now we need to know
                #if the element is over a certain times called
                if stateelement.TimesCalled > DuplicateAmountDepth:
                    #This state is overused. We need to go a level deeper,
                    #this means lengthening the state with the rest
                    #and calling the recursion again
                    newp = stateelement
                    news = s + TextDrain[0]
                    TextDrain = TextDrain[1:]
                    newr = TextDrain
                    stateRestCompareRecursive(newp, news, newr)
                #if it is not overused, it is a good state, and now we should
                #find the outcome
                findOutcomeForPart(stateelement, s, r)
    #we were unable to find the state, we will write it now
    if check == "false":
        newpart = TextPart(s)
        print("Wrote State: " + s + " To Part: " + str(p.ThisElement))
        p.NextElements.append(newpart)
        #newpart.NextElements = []
        #newpart.Outcomes = []
        findOutcomeForPart(newpart, s, r)
        

#finds the appropriate outcome for a given state
#part, state, rest
def findOutcomeForPart(p, s, r):
    global TopTextPart
    global TextDrain
    if len(TextDrain) > 1:
        
        newoutcome = TextDrain[0]
        TextDrain = TextDrain[1:]
        newr = TextDrain
        findOutcomeForPartRecursive(TopTextPart, s, newr, newoutcome, p) 

#statepart is the part which is holding the current state.
#p is the search through the list to find whether or not the outcome
#really exists. o gets lengthened every time we loop
def findOutcomeForPartRecursive(p, s, r, o, statepart):
    check = "false"
    global TextDrain
    #print("My o value: " + str(o))
    for stateelement in p.NextElements:
        #for all the potential states in the next area
        if o == stateelement.ThisElement:
            #we found a match, so try the next thing and see if that matches
            if len(r) > 1:
                newo = o + r[0]
                newr = r[1:]
                
                check = "true"
                p.TimesCalled = p.TimesCalled + 1
                findOutcomeForPartRecursive(stateelement, s, newr, newo, statepart)
            else:
                #We've run out of lines, don't do anything
                check = "qqq"
                #we didn't write an outcome
    #we were unable to find a match, so we will use what we have in
    #our current part and call it a day
    if check == "false":
        if len(o) > 1:
            #We've gone through the loop already
            p.TimesCalled = p.TimesCalled + 1
            writeStateOutcomeToPart(p, s, o[:-1], statepart)
        else:
            #this is the case with one new character
            p.TimesCalled = p.TimesCalled + 1
            writeStateOutcomeToPart(p, s, o, statepart)


def writeStateOutcomeToPart(p, s, o, statepart):
    check = "false"
    #if the outcome already exists, we add to the outcome there
    for outcome in statepart.Outcomes:
        if outcome.Value == o:
            print("Outcome match found with Value: " + outcome.Value + " and o: " + o)
            check = "true"
            outcome.TimesCalled = outcome.TimesCalled + 1
    #if the outcome does not exist, we make a new one
    if check == "false":
        myoutcome = Outcome(o)
        statepart.Outcomes.append(myoutcome)
    #whatever happens, give me a new saved state
    print("State: " + s + " Outcome: " + o)
    print("Used State: " + statepart.ThisElement)
    global SavedState
    SavedState = o
    #also, decrement the text drain by the length of my saved state
    somelength = len(o)
    global TextDrain
    s = slice(somelength-1, len(TextDrain))
    TextDrain = TextDrain[s]
    print("new drain length " + str(len(TextDrain)))
    
def DEBUGPrintTree(part):
    print(str(part.ThisElement))
    for p in part.NextElements:
        printTreeHelp(p, "  ")
        

def printTreeHelp(p, spaces):
    print(spaces + str(p.ThisElement))
    for sp in p.NextElements:
        printTreeHelp(sp, spaces + "  ")

def findPart(somestate):
    global TopTextPart
    return findPartHelp(somestate, somestate, TopTextPart, 0)

def findPartHelp(somestate, fullstate, part, indexcheck):
    if fullstate == part.ThisElement:
        return part
    else:
        for ele in part.NextElements:
            if somestate[0] == ele.ThisElement[indexcheck]:
                return findPartHelp(somestate[1:], fullstate, ele, indexcheck + 1)
    print("No Part Found")

#main
    """
def main():
    print("Main has begun. Retrieving XML")
    getXML("CALLIEMachine.xml")
    print("XML Get complete, opening files")
    print(os.curdir)
    openReadAllTxt('Stories')
    saveXML("CALLIEMachine.xml")
    closeTxt()
    print("Completed!")
    """
#CM is a path to a CallieMachine, FileLoc is the path to the text file
def readTextFile(FileLoc, CM):
    getXML(CM)
    openTxt(FileLoc)
    readTxtFile()
    saveXML(CM)
    closeTxt()
    print("Read one Text File!")
    

def readFilesInFolder(FolderLoc, CM):
    getXML(CM)
    openReadAllTxt(FolderLoc)
    saveXML(CM)
    closeTxt()
    print("Read All Files in Folder!")

def readStringList(StringList, CM):
    getXML(CM)
    global TextData
    for sometext in StringList:
        TextData = sometext
        readTxtFile()
    saveXML(CM)
    print("ReadStringList")
    
    

#The whole point of this is I need to be able to pass it something, and it needs to
#read it and put it in the xml doc.        
#for i in range(0, 15):
#main()

