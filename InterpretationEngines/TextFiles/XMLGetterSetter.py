import TextPartClass
import xml.etree.ElementTree as ET

#Gets an XML file I guess. Returns a textpart
def getXMLReturnTP(path):
    MyTextPart = TextPartClass.TextPart("")
    tree = ET.parse(path)
    root = tree.getroot()
    MyTextPart.TimesCalled = int(root[0][1].text)
    populateTreeForPart(MyTextPart, root[0])
    return MyTextPart


def populateTreeForPart(part, element):
    for nextpart in element[2]:
        newpart = TextPartClass.TextPart(nextpart[0].text)
        newpart.TimesCalled = int(nextpart[1].text)
        for potoutcome in nextpart[3]:
            newoutcome = TextPartClass.Outcome(potoutcome[0].text)
            newoutcome.TimesCalled = int(potoutcome[1].text)
            newpart.Outcomes.append(newoutcome)
        part.NextElements.append(newpart)
        populateTreeForPart(newpart, nextpart)


#Saves the XML File out based on the whole TextParts
def saveXML(path, MyTextPart):
    import xml.etree.cElementTree as NET
    cleanData(MyTextPart)
    root = NET.Element("root")
    TPtree = NET.SubElement(root, "TextPart")
    WritePartsRecursively(NET, TPtree, MyTextPart)
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

def cleanData(TP):
    cleanUnusedOutcomes(TP)

def cleanUnusedOutcomes(TP):
    cleanUnusedOutcomesRecursive(TP)

def cleanUnusedOutcomesRecursive(textpart):
    for tp in textpart.NextElements:
        if len(tp.NextElements) > 0:
            textpart.Outcomes = []
            cleanUnusedOutcomesRecursive(tp)
