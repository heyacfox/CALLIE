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

    #HasPartHuh: Returns whether a TextPart's string is SOMEHWERE in the TP tree
    def hasPartHuh(self, stringTotal):
            hasPartHuhRecursive(self, stringTotal, stringTotal, 0)


    def hasPartHuhRecursive(myTextPart, stringPart, stringTotal, index):
        if stringTotal == self.ThisElement:
            return true
        else:
            for ele in myTextPart.NextElements:
                if stringPart[0] == ele.ThisElement[index]:
                    return hasPartHuhRecursive(ele, stringPart[1:], stringTotal, index + 1)
        return false
        
    #FindPart: ONLY RUN THIS AFTER YOU'VE CHECKED THE PART EXISTS
    def findPart(self, stringTotal):
        findPartRecursive(self, stringTotal, stringTotal, 0)

    def findPartRecursive(myTextPart, stringPart, stringTotal, index):
        if stringTotal == self.ThisElement:
            return myTextPart
        else:
            for ele in myTextPart.NextElements:
                if stringPart[0] == ele.ThisElement[index]:
                    return findPartRecursive(ele, stringPart[1:], stringTotal, index + 1)


class Outcome:
    Value = ""
    TimesCalled = 0

    def __init__(self, somevalue):
        self.Value = somevalue
        self.TimesCalled = 1
