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

    def test_adept_reader(self):
        text_story_cleaner = clean_text_story.TextStoryCleaner()
        text_story_consumer = consume_text_story.TextStoryConsumer()
        adept_reader_text = adept_reader.AdeptReader(0.00)
        newarray = text_story_cleaner.clean_text_story('documents/mobydick.txt')
        new_consume = text_story_consumer.consume_text_list(newarray)
        adept_reader_text.add_to_memory(new_consume)
        knowthis = adept_reader_text.do_I_know_this(new_consume)
        print(knowthis)
        self.assertEqual(1.0, knowthis)

        wolfarray = text_story_cleaner.clean_text_story('documents/wolf2.txt')
        wolfconsume = text_story_consumer.consume_text_list(wolfarray)
        print(adept_reader_text.do_I_know_this(wolfconsume))
        self.assertNotAlmostEqual(adept_reader_text.do_I_know_this(wolfconsume), 1.0)





if __name__ == '__main__':
    unittest.main()
    #MyTestCase.test_something()
    #MyTestCase.test_adept_reader()
