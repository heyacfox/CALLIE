class TextStoryCleaner:

    def __init__(self):
        lower_case_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                            "x", "y", "z"]
        upper_case_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
                            "X", "Y", "Z"]
        symbols_in_words = ["'"]
        self.valid_word_parts = lower_case_chars + upper_case_chars + symbols_in_words

    #Assumes we can already access the text as a txt file locally
    def clean_text_story(self, textLocation):
        #take in unstructured text that is story-like
        word_tracking = ""
        symbol_tracking = ""
        tracking_word = True
        outputarray = []
        text_file = open(textLocation, "r")
        for line in text_file:
            for ch in line:
                if ch in self.valid_word_parts:
                    if symbol_tracking != "":
                        outputarray.append(symbol_tracking)
                        symbol_tracking = ""
                    word_tracking = word_tracking+ch
                else:
                    if word_tracking != "":
                        outputarray.append(word_tracking)
                        word_tracking = ""
                    symbol_tracking = symbol_tracking + ch

        #handles some basic removes that we need done
        outputarray = [x for x in outputarray if x not in [" ", "\n"]]

        #fancy replaces
        symbolplusnewlinereplaces = ['. ', ';', '.', ',', '--', '"']
        for s in symbolplusnewlinereplaces:
        #    for o in outputarray:
        #        if len(o) < 4:
        #            o.replace(s + '\n', s + ' ')
            outputarray = [w.replace(s + '\n', s + ' ') for w in outputarray]
        outputarray = [w.replace('\n', '\n\n') for w in outputarray]

        text_file.close()
        #Turn it into a collection of words and symbols in a specific order
        #Return the array of units to be used as input to something else
        return outputarray

    def count_parts(self, textLocation):
        outputarray = self.clean_text_story(textLocation)
        outputdict = {}
        for part in outputarray:
            if part in outputdict.keys():
                outputdict[part] = outputdict[part] + 1
            else:
                outputdict[part] = 1
        return outputdict


