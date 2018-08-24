import unicodedata

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
        text_file = open(textLocation, "r", encoding="utf8")
        #text_file
        for line in text_file:
            #print(line)
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

    def meta_cleanup(self, text):
        gutenberg_header = "START OF THIS PROJECT GUTENBERG EBOOK"
        gutenberg_footer = "END OF THIS PROJECT GUTENBERG EBOOK"
        if gutenberg_header in text:
            text = self.gutenberg_meta_cleanup_header(text)
        if gutenberg_footer in text:
            text = self.gutenberg_meta_cleanup_footer(text)
        return text

    def gutenberg_meta_cleanup_header(self, text):
        gutenberg_header = "START OF THIS PROJECT GUTENBERG EBOOK"
        matchnum = "nothing"
        for num, line in enumerate(text.split('\n'), 1):
            #print(line)
            if gutenberg_header in line:
                matchnum = num
        #print(str(matchnum))
        #matched_lines = [line for line in text.split('\n') if gutenberg_header in line]
        #header_row = matched_lines[0]
        text_split = text.split('\n')
        text_after_header = text_split[matchnum:]
        #print ("textafter:[" + text_after_header[0] + "]")
        text_checking = text_after_header[0]
        while text_checking == '':
            #print("TextChecking:[" + text_checking + "]")
            text_after_header = text_after_header[1:]
            text_checking = text_after_header[0]
        rejoined = '\n'.join(text_after_header)
        #print(rejoined)
        return rejoined

    def gutenberg_meta_cleanup_footer(self, text):
        gutenberg_footer = "END OF THIS PROJECT GUTENBERG EBOOK"
        matchnum = "nothing"
        for num, line in enumerate(text.split('\n'), 1):
            if gutenberg_footer in line:
                matchnum = num
        #matched_lines = [line for line in text.split('\n') if gutenberg_footer in line]
        #footer_row = matched_lines[0]
        #print(str(matchnum))
        text_split = text.split('\n')
        text_before_footer = text_split[:(matchnum - 1)]
        #print("textbefore:[" + text_before_footer[-1] + "]")
        textchecking = ''
        while textchecking == '':
            #print("TextChecking:[" + textchecking + "]")
            text_before_footer = text_before_footer[:-2]
            textchecking = text_before_footer[-1:]
        text_before_footer = text_before_footer[:-1]
        rejoined = '\n'.join(text_before_footer)
        #print(rejoined)
        #print("Line after")
        return rejoined
