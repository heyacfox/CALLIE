import random
import copy
import re
from Consumers import consume_text_story

class AdeptReader:
    #this CAM reads content and stores that as information
    #Then, after reading something new, will determine whether or not it likes that new content
    #based on the content that it has already read
    def __init__(self, lossiness):
        self.memory = {}
        #lose x% of your memory every time you consume something
        self.lossiness = lossiness
        # after x entries in the key value list, consolidate that into a new key
        self.consolidation_filter = 3
        self.consumer = consume_text_story.TextStoryConsumer()

    def do_I_know_this(self, newcorpus):
        #corpuses are the dictionary outputs that consumers give you
        #check new corpus against memory. If keys/values are present within memory, then you know this already
        memorykeys = list(self.memory.keys())
        #you need to count how many key/values you need to check for
        newcount = 0
        for k in newcorpus.keys():
            newcount = newcount + len(newcorpus[k])

        matchcount = 0
        #now with that total count, we're going to see what % match we get against memory
        for partmap in newcorpus.keys():
            if partmap in memorykeys:
                memoryparts = self.memory[partmap]
                for partmapvalue in newcorpus[partmap]:
                    if partmapvalue in memoryparts:
                        matchcount = matchcount + 1

        return matchcount / newcount

    def add_to_memory(self, new_consume):

        memorykeys = list(self.memory.keys())
        print("Keys we have now:" + str(len(memorykeys)))

        for part in new_consume:
            if part in memorykeys:
                self.memory[part] = self.memory[part] + copy.deepcopy(new_consume[part])
            else:
                self.memory[part] = copy.deepcopy(new_consume[part])
        print("Add to memory completed")

    def add_to_memory_lossy_consolidation(self, clean_text):
        self.consolidate_phrases()
        new_consume = self.consumer.consume_with_consolidation(clean_text, self.memory)
        self.add_to_memory(new_consume)

        lose_items = int(self.count_memory_items() * self.lossiness)
        print("Consolidating Phrases...")

        print("Forgetting " + str(lose_items) + "items")

        for x in range(lose_items):
            self.remove_random_memory_item_safely()

        # this will cause us to forget phrases we just consolidated without repetition and we gotta live with that

        print("Keys we have after cleanup:" + str(len(list(self.memory.keys()))))

    def add_to_memory_lossy(self, new_consume):
        #consolidate at the beginning and maybe my memory won't be terrible?
        self.consolidate_phrases()
        #NO THE CONSUMER NEEDS THE CONSOLIDATION FOR THE CONSUME ACTION
        self.add_to_memory(new_consume)
        #count how many items you need to lose based on lossiness
        lose_items = int(self.count_memory_items() * self.lossiness)
        print("Consolidating Phrases...")

        print("Forgetting " + str(lose_items) + "items")

        for x in range(lose_items):
            self.remove_random_memory_item()

        keys_to_remove = []
        for key in self.memory.keys():
            if len(list(self.memory[key])) <= 0:
                keys_to_remove.append(key)
        for remove_key in keys_to_remove:

            del self.memory[remove_key]

        #this will cause us to forget phrases we just consolidated without repetition and we gotta live with that

        print("Keys we have after cleanup:" + str(len(list(self.memory.keys()))))

    def remove_random_memory_item(self):
        try:
            memorykeys = list(self.memory.keys())
            randomkey = random.choice(memorykeys)
            if len(self.memory[randomkey]) <= 0:
                del self.memory[randomkey]
            else:
                memoryvalues = list(self.memory[randomkey])
                randomvalue = random.choice(memoryvalues)
                self.memory[randomkey].remove(randomvalue)
        except IndexError:
            print("Index Error on remove attempt")
            print("Key set to use:" + randomkey)
            print("List at key" + str(self.memory[randomkey]))

    def remove_random_memory_item_safely(self):
        #if there's only 1 item in the values list, give up on the removal action
        memorykeys = list(self.memory.keys())
        randomkey = random.choice(memorykeys)
        if len(self.memory[randomkey]) <= 1:
            return
        else:
            memoryvalues = list(self.memory[randomkey])
            randomvalue = random.choice(memoryvalues)
            self.memory[randomkey].remove(randomvalue)

    def count_memory_items(self):
        memoryCount = 0
        for k in self.memory.keys():
            memoryCount = memoryCount + len(self.memory[k])
        return memoryCount

    def consolidate_phrases(self):
        keys_to_add = []
        for key in self.memory.keys():
            #look through all values
            #if any have duplicates equal or greater than consolidation filter, make a new key for that.
            #HOW DO I STOP FROM DELETING THESE FROM MEMORY
            outputdict = {}
            for part in self.memory[key]:
                if part in outputdict.keys():
                    outputdict[part] = outputdict[part] + 1
                else:
                    outputdict[part] = 1
            for checkkey in outputdict.keys():
                if outputdict[checkkey] >= self.consolidation_filter:
                    if self.should_I_add_a_space(key[-1:], checkkey[0]):
                        keys_to_add.append(key + " " + checkkey)
                    else:
                        keys_to_add.append(key + checkkey)
                    self.memory[key] = [x for x in self.memory[key] if x not in [checkkey]]
                    #that specific value will NEVER get used again with that key, because the phrase will pick it up instead
        for newkey in keys_to_add:
            self.memory[newkey] = []
        #print("keys added:" + str(keys_to_add))

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


