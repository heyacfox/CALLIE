import xml.etree.ElementTree as ET

#FIRST TWEET ID
global firstTweetID
firstTweetID = "555868232993628162"

#returns the integer value as found in the XML file.
def lastID():
    tree = pullIdXML()
    root = tree.getroot()
    myvalue = root[0].text
    return int(myvalue)

#Rewrites the value in the XML file
def rewriteLastID(idvalue):
    import xml.etree.cElementTree as NET
    root = pullIdXML().getroot()
    root[0].text = str(idvalue)
    tree = NET.ElementTree(root)
    tree.write("somexml.xml")
    
def resetIDtoStart():
    import xml.etree.cElementTree as NET
    root = pullIdXML().getroot()
    global firstTweetID
    root[0].text = firstTweetID
    tree = NET.ElementTree(root)
    tree.write("somexml.xml")

def pullIdXML():
    tree = ET.parse("somexml.xml")
    return tree

def returnFromX():
    tree = pullIdXML()
    root = tree.getroot()
    myvalue = root[1].text
    return int(myvalue)

def returnToY():
    tree = pullIdXML()
    root = tree.getroot()
    myvalue = root[2].text
    return int(myvalue)

def returnXYCur():
    tree = pullIdXML()
    root = tree.getroot()
    myvalue = root[3].text
    return int(myvalue)

def setXYCur(idvalue):
    import xml.etree.cElementTree as NET
    root = pullIdXML().getroot()
    root[3].text = str(idvalue)
    tree = NET.ElementTree(root)
    tree.write("somexml.xml")
