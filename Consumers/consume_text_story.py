import re
import logging

class TextStoryConsumer:


    def __init__(self):
        self.something = 1
        logging.basicConfig(filename='consume.log', level=logging.DEBUG, filemode='w')


    #output of this will be the tree heirarchy that can be used as input to a creator

    def consume_text_list(self, text_list):
        #cycle along each specific part
        #you have a current, and the prev
        #link the current to the prev, reset the prev
        prev_part = text_list[0]
        text_list = text_list[1:]
        output_dict = {}
        for part in text_list:
            if prev_part not in output_dict.keys():
                output_dict[prev_part] = [part]
            else:
                output_dict[prev_part] = output_dict[prev_part] + [part]
            prev_part = part
        return output_dict

    def consume_with_consolidation(self, text_list, consolidator):
        print ("List of text to analyze" + str(len(text_list)))

        #logging.debug("Starting a Consume with" + str(len(text_list)) + " parts")
        #logging.debug("Consolidator keys:" + str(consolidator.keys()))
        if(len(text_list) < 2):
            #this text is unreadable, since it only has one part
            return
        prev_part = text_list[0]
        curr_part = ""
        printevery = 5000
        output_dict = {}
        text_list = text_list[1:]
        for x in range(len(text_list)):
            if (x % printevery == 0):
                print ("Text Remaining:" + str(len(text_list) - x))
            curr_part = text_list[x]
            combinecheck = ""
            if self.should_I_add_a_space(prev_part[-1:], curr_part[0]):
                combinecheck = prev_part + " " + curr_part
                #logging.debug("Added space to combine for:" + combinecheck)
            else:
                combinecheck = prev_part + curr_part
            if self.phrase_has_keysection(consolidator, combinecheck):
                prev_part = combinecheck
                #logging.debug("Using Combine as Prev:" + combinecheck)
            else:
                if prev_part not in output_dict:
                    output_dict[prev_part] = [curr_part]
                else:
                    output_dict[prev_part] = output_dict[prev_part] + [curr_part]
                prev_part = curr_part

        return output_dict



    def phrase_has_keysection(self, consolidator, key_to_check):
        if key_to_check in consolidator.keys():
            #logging.debug("Phrase found:" + key_to_check)
            #print ("Phrase found:" + key_to_check)
            return True
        else:
            #logging.debug("Phrase not found:" + key_to_check)
            return False

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