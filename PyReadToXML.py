#! usr/bin/python
# -*- coding: utf-8 -*-

import XMLGetterSetter
import TextPartClass
import os
#---------------------
#Constatnts
global DuplicateAmountDepth
DuplicateAmountDepth = 20
global StringCounterMax
StringCounterMax = 100

#------------------
#Global Variables
global StringRest
global SavedState
global GlobalTopTextPart
global StringCounter
StringCounter = 0



#-------------------------------
#Basics. Here, are the public functions



#Returns Nothing. Alters the CM from reading
#the text file at the File Location
def readTextFile(FileLoc, CM):
    TopTextPart = XMLGetterSetter.getXMLReturnTP(CM)
    newTP = readTextFileToPart(FileLoc, TopTextPart)
    XMLGetterSetter.saveXML(CM, newTP)
    print("Complete")



#Returns nothing. Reads all text files in a given folder
def readFilesInFolder(FolderLoc, CM):
    TopTextPart = XMLGetterSetter.getXMLReturnTP(CM)
    for myfile in os.listdir(FolderLoc):
        print("Reading:"+myfile)
        TopTextPart = readTextFileToPart(FolderLoc + "/" + myfile, TopTextPart)
    XMLGetterSetter.saveXML(CM, TopTextPart)
    print("Complete")
    


#Reads all strings in a list
def readStringList(StringList, CM):
    TopTextPart = XMLGetterSetter.getXMLReturnTP(CM)
    print("ReadingStrings")
    for s in StringList:
        readStringtoPart(s, TopTextPart)
    print("Saving XML")
    XMLGetterSetter.saveXML(CM, TopTextPart)
    print("Complete")


#Reads a string to the CM
def readString(MyString, CM):
    TopTextPart = XMLGetterSetter.getXMLReturnTP(CM)
    newTP = readStringtoPart(MyString, TopTextPart)
    XMLGetterSetter.saveXML(CM, newTP)
    print("Complete")

#-------------------------------
#These functions are private


def readTextFileToPart(FileLoc, TP):
    #toReadText is a string
    ToReadText = openTxt(FileLoc)
    if len(ToReadText) > 10000:
        los = splitStringToChunks(ToReadText)
        for s in los:
            TP = readStringtoPart(s, TP)
        return TP
    else:
        return readStringtoPart(ToReadText, TP)

def splitStringToChunks(MyString):
    chunks = len(MyString)
    chunkSize = len(MyString)//10
    return [MyString[i:i+chunkSize] for i in range(0, chunks, chunkSize)]

#returns a string of the text
def openTxt(FileLoc):
    TextFile = open (FileLoc, "r")
    return TextFile.read()

#takes a string, applies it to the text part, returns a textpart
def readStringtoPart(StringtoRead, TP):
    if len(StringtoRead) > 0:
        StateToPass = StringtoRead[0]
        global StringRest
        global SavedState
        global GlobalTopTextPart
        GlobalTopTextPart = TP
        SavedState = StateToPass
        StringRest = StringtoRead[1:]
        #print(SavedState)
        while len(StringRest) > 1:
            printlengthevery()
            #print("State Using:" + SavedState)
            #print("Rest:" + StringRest)
            createStateCompareEvalTop(SavedState, StringRest, TP)
    return TP

def createStateCompareEvalTop(state, rest, textpart):
    if len(state) == 1:
        #print("compareevalbranch1")
        stateRestCompareRecursive(state, rest, textpart)
    else:
        stateRestCompareRecursive(state, rest, findPart(state))

def printlengthevery():
    global StringRest
    global StringCounter
    global StringCounterMax
    if StringCounter > StringCounterMax:
        StringCounter = 0
        print("Length of Rest:" + str(len(StringRest)))
    else:
        StringCounter = StringCounter + 1

#This function ALTERS THE textpart. You might get through the whole thing
#and decide NOT to alter the textpart, which is totally okay. It will jus come back up to 
def stateRestCompareRecursive(state, rest, textpart):
    global DuplicateAmountDepth
    global StringRest
    PartFoundHuh = False
    if state == textpart.ThisElement:
        if textpart.TimesCalled > DuplicateAmountDepth:
            #This state has been overused. We need to make a new state IF THE REST EXISTS
            if len(rest) > 1:
                #This means we can expand the state, and potentially still get a 1 character outcome back
                news = state + rest[0]
                StringRest = StringRest[1:]
                stateRestCompareRecursive(news, rest[1:], textpart)
            #If we hit this else, we come back to the top and we leave
            else:
                StringRest = ""
        #if not overused, get the outcome for it
        else:
            writeOutcomeToPart(textpart, findOutcomeForPart(rest, textpart, textpart))
        PartFoundHuh = True

    #We're at this next if our state is NOT equal to the text part's
    #value (and we have a state more than 1) IF I HAVEN'T GONE FAR ENOUGH DOWN
    else:
        for onetp in textpart.NextElements:
            if state == onetp.ThisElement:
                #we found a match. Run StateREstCompareRecursive to
                #get the match on that
                PartFoundHuh = True
                stateRestCompareRecursive(state, rest, onetp)
        
    #the there were no matches found in the nextelements, write a new state
    if PartFoundHuh == False:
        #print("MakingNewPart")
        newpart = TextPartClass.TextPart(state)
        textpart.NextElements.append(newpart)
        writeOutcomeToPart(newpart, findOutcomeForPart(rest, newpart, textpart))
            
#GIVE ME BACK AN OUTCOME PLEASE
def findOutcomeForPart(rest, newtextpart, oldtextpart):
    global StringRest
    global GlobalTopTextPart
    if len(rest) > 1:
        newoutcome = rest[0]
        newr = rest[1:]
        StringRest = StringRest[1:]
        return findOutcomeForPartRecursive(newr, newoutcome, GlobalTopTextPart)
    #If our newtextpart didn't end up getting an outcome, kill it from oldtextpart
    #and call it a day
    elif len(newtextpart.Outcomes) == 0:
        oldtextpart.NextElements.remove(newtextpart)
        return ''

#The whole point of this was that we cycle down as far as we can in the existing
#states to write our outcome
def findOutcomeForPartRecursive(rest, outcome, breakingdownpart):
    global StringRest
    #print("Outcome for This Lel:" + outcome)
    for innertp in breakingdownpart.NextElements:
        if outcome == innertp.ThisElement:
            #we found a match, now can we go deeper?
            if len(rest) > 0:
                newoutcome = outcome + rest[0]
                newrest = rest[1:]
                #WE'lll...wait on decrementing the StringRest until we WRITE
                #the outcome and use it as our new state
                breakingdownpart.TimesCalled = breakingdownpart.TimesCalled + 1
                #now let's check the next level
                return findOutcomeForPartRecursive(newrest, newoutcome, innertp)
    #If we get here, there are no nextelements that we could potentially
    #use as out outcome, so we have to settle for what we have.
    breakingdownpart.TimesCalled = breakingdownpart.TimesCalled + 1
    if len(outcome) > 1:
        #we need to go back because there existed no state for this combination
        #of letters, but there was for the previous one.
        return outcome[:-1]
    else:
        #we couldn't find a single letter state that existed. That was sad.
        return outcome
        

def writeOutcomeToPart(textpart, outcome):
    #IF THE OUTCOME IS '', Don't WRITE ANYTHING
    global StringRest
    #print("writing State:" + textpart.ThisElement + "|To:" + outcome)
    if outcome != '':
        #print("Now Writing Outcome")
        for myoutcome in textpart.Outcomes:
            if myoutcome.Value == outcome:
                myoutcome.TimesCalled = myoutcome.TimesCalled + 1
        if outcome not in textpart.Outcomes:
            mynewoutcome = TextPartClass.Outcome(outcome)
            textpart.Outcomes.append(mynewoutcome)
        global SavedState
        lengthofoutcome = len(outcome)
        SavedState = outcome
        slic = slice(lengthofoutcome-1, len(StringRest))
        StringRest = StringRest[slic]
    else:
        #Otherwise, we got to the end, set the rest to 0 so we give up
        StringRest = ""

def findPart(state):
    global GlobalTopTextPart
    return findPartRecursive(state, state, GlobalTopTextPart, 0)

def findPartRecursive(somestate, fullstate, textpart, indexcheck):
    if fullstate == textpart.ThisElement:
        return textpart
    else:
        for lowertextpart in textpart.NextElements:
            if somestate[0] == lowertextpart.ThisElement[indexcheck]:
                return findPartRecursive(somestate[1:], fullstate, lowertextpart, indexcheck + 1)



