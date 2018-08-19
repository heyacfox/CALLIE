import random
import re

class TextStoryCreator():

    def __init__(self):
        self.something = 1

    def create_text_story(self, mappings, length):
        text_string = ""
        mappingsKeys = list(mappings.keys())
        rc = random.choice(mappingsKeys)
        text_string = text_string + rc
        #mappingsLength = mappingsKeys.count()
        for x in range(length):
            #pick a random key, then a random value from that key
            mappingsvalues = mappings[rc]
            mappingvaluechosen = random.choice(mappingsvalues)
            if self.should_I_add_a_space(rc, mappingvaluechosen):
                text_string = text_string + " " + mappingvaluechosen
            else:
                text_string = text_string + mappingvaluechosen


            rc = mappingvaluechosen
        return text_string

    def should_I_add_a_space(self, prev_word, cur_word):
        searchValuePrev = re.search('[a-zA-Z]', prev_word)
        searchValueCurr = re.search('[a-zA-Z]', cur_word)
        #if the prev_word is a word, and cur_word is a word, add a space
        if searchValueCurr is not None and searchValuePrev is not None:
            return True
        if searchValuePrev is None and searchValueCurr is not None:
            return False
        if searchValuePrev is not None and searchValueCurr is None:
            return False
        if searchValuePrev is None and searchValueCurr is None:
            return False
        #If prev_word is a symbol, and cur_word is a word, don't add a space
        #if prev_word is a word, and curr_word is a symbol, don't add a space
