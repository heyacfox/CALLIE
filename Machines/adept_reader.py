import random

class AdeptReader:
    #this CAM reads content and stores that as information
    #Then, after reading something new, will determine whether or not it likes that new content
    #based on the content that it has already read
    def __init__(self, lossiness):
        self.memory = {}
        #lose x% of your memory every time you consume something
        self.lossiness = lossiness

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
        for part in new_consume:
            if part in memorykeys:
                self.memory[part] = self.memory[part] + new_consume[part]
            else:
                self.memory[part] = new_consume[part]

    def add_to_memory_lossy(self, new_consume):
        self.add_to_memory(new_consume)
        #count how many items you need to lose based on lossiness
        lose_items = int(self.count_memory_items() * self.lossiness)

        for x in range(lose_items):
            self.remove_random_memory_item()

    def remove_random_memory_item(self):
        memorykeys = list(self.memory.keys())
        randomkey = random.choice(memorykeys)
        memoryvalues = list(self.memory[randomkey])
        randomvalue = random.choice(memoryvalues)
        self.memory[randomkey].remove(randomvalue)



    def count_memory_items(self):
        memoryCount = 0
        for k in self.memory.keys():
            memoryCount = memoryCount + len(self.memory[k])

