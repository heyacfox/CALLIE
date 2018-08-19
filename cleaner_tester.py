import unittest
from Cleaners import clean_text_story
from Consumers import consume_text_story
from Creators import create_text_story
from Machines import adept_reader
from collections import OrderedDict
from operator import itemgetter
import os


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     text_story_cleaner = clean_text_story.TextStoryCleaner()
    #     text_story_consumer = consume_text_story.TextStoryConsumer()
    #     text_story_creator = create_text_story.TextStoryCreator()
    #     for filename in os.listdir(os.getcwd() + "\\documents"):
    #         newarray = text_story_cleaner.clean_text_story('documents/' + filename)
    #         newdict = text_story_cleaner.count_parts('documents/' + filename)
    #         consume_dict = text_story_consumer.consume_text_list(newarray)
    #         finalstory = text_story_creator.create_text_story(consume_dict, 5000)
    #         #print (finalstory)
    #         #print(newdict)
    #         #print(newarray)
    #         #print(OrderedDict(sorted(newdict.items(), key=itemgetter(1), reverse=True)))
    #         #print(consume_dict)


        #array1 = ["Hi", " ", "No", " "]
        #array2 = ["Hi", "No"]
        #print(array1)
        #print(array2)
        #array1.remove(" ")
        #print(array1)
        #newarray.remove(" ")
        #print(newarray.count(" "))

        #self.assertEqual(array1.count(" "), 0)
        #self.assertEqual(0, newarray.count(" "))

    # def test_adept_reader(self):
    #     text_story_cleaner = clean_text_story.TextStoryCleaner()
    #     text_story_consumer = consume_text_story.TextStoryConsumer()
    #     adept_reader_text = adept_reader.AdeptReader(0.00)
    #     newarray = text_story_cleaner.clean_text_story('documents/mobydick.txt')
    #     new_consume = text_story_consumer.consume_text_list(newarray)
    #     adept_reader_text.add_to_memory(new_consume)
    #     knowthis = adept_reader_text.do_I_know_this(new_consume)
    #     print(knowthis)
    #     self.assertEqual(1.0, knowthis)
    #
    #     wolfarray = text_story_cleaner.clean_text_story('documents/wolf2.txt')
    #     wolfconsume = text_story_consumer.consume_text_list(wolfarray)
    #     print(adept_reader_text.do_I_know_this(wolfconsume))
    #     self.assertNotAlmostEqual(adept_reader_text.do_I_know_this(wolfconsume), 1.0)

    def non_test_consolidation_works(self):
        adept_reader_text_non_lossy = adept_reader.AdeptReader(0.00)
        text_story_consumer = consume_text_story.TextStoryConsumer()
        test_story_array = ["I", "am","a","very","powerful","person","when","I","jump","over","a","very","powerful","obstacle"]
        for x in range(10):
            new_consume = text_story_consumer.consume_with_consolidation(test_story_array, adept_reader_text_non_lossy.memory)
            adept_reader_text_non_lossy.add_to_memory_lossy(new_consume)

        #print(adept_reader_text_non_lossy.memory.keys())
        self.assertIn("I am", adept_reader_text_non_lossy.memory.keys())



    def test_lossy(self):
        text_story_cleaner = clean_text_story.TextStoryCleaner()
        text_story_consumer = consume_text_story.TextStoryConsumer()
        text_story_creator = create_text_story.TextStoryCreator()
        adept_reader_text_non_lossy = adept_reader.AdeptReader(0.00)
        adept_reader_text_slightly_lossy = adept_reader.AdeptReader(0.02)
        adept_reader_text_semi_lossy = adept_reader.AdeptReader(0.05)
        adept_reader_text_very_lossy = adept_reader.AdeptReader(0.10)
        adept_reader_text_super_lossy = adept_reader.AdeptReader(0.20)
        readers2 = [adept_reader_text_non_lossy, adept_reader_text_semi_lossy,
                   adept_reader_text_slightly_lossy, adept_reader_text_super_lossy,
                   adept_reader_text_very_lossy]

        readers = [adept_reader_text_slightly_lossy]




        for ar in readers:
            print("Lossy Amount=" + str(ar.lossiness))
            for filename in os.listdir(os.getcwd() + "\\documents"):
                print("reading:" + filename)
                for x in range(3):
                    ar.add_to_memory_lossy_consolidation(text_story_cleaner.clean_text_story('documents/' + filename))

            print(text_story_creator.create_text_story(ar.memory, 1000))

        self.assertEqual(True, True)




if __name__ == '__main__':
    unittest.main()
    #MyTestCase.test_something()
    #MyTestCase.test_adept_reader()
