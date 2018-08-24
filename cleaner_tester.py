import unittest
from Cleaners import clean_text_story
from Consumers import consume_text_story
from Creators import create_text_story
from Machines import adept_reader
from Collectors import gutenberg_collector
from collections import OrderedDict
from operator import itemgetter
import os
import re


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



    def non_test_lossy(self):
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

    def non_test_gutenberg_meta_cleanups(self):
        text_story_cleaner = clean_text_story.TextStoryCleaner()
        #basepath = 'documents_downloaded/'
        #text12path = basepath + '12.txt'
        #text12file = open(text12path, "r", encoding="utf8")
        #text12contents = text12file.read()
        #text12cleanedactual = text_story_cleaner.meta_cleanup(text12contents)
        #text12exptpath = 'manual_test_checks/12-gutenberg_meta.txt'
        #text12exptfile = open(text12exptpath, "r", encoding="utf8")
        #text12exptcontents = text12exptfile.read()
        #text12file.close()
        #text12exptfile.close()
        #self.assertEqual(text12cleanedactual, text12exptcontents)
        gutenberg_meta_files = []
        #if we find a file in the manual tests folder with '-gutenberg_meta' as a name
        for manual_file_name in os.listdir(os.getcwd() + "\\manual_test_checks"):
            if '-gutenberg_meta' in manual_file_name:
                gutenberg_meta_files.append(manual_file_name)
        for gutenberg_file in gutenberg_meta_files:
            print("Gutenberg masnual file is:" + gutenberg_file)
            download_name_list = gutenberg_file.split('-gutenberg_meta')
            download_name = ''.join(download_name_list)
            download_file_path = 'documents_downloaded/' + download_name
            opened_file = open(download_file_path, "r", encoding="utf8")
            file_contents = opened_file.read()
            opened_file.close()
            file_meta_cleaned = text_story_cleaner.meta_cleanup(file_contents)
            manual_check_path = 'manual_test_checks/' + gutenberg_file
            manual_file_opened = open(manual_check_path, "r", encoding="utf8")
            manual_file_contents = manual_file_opened.read()
            manual_file_opened.close()
            self.assertEqual(manual_file_contents, file_meta_cleaned)

    def test_how_many_gutenberg_cleanups(self):
        print("GUTENBERG CLEANUP COUNT CHECK")
        non_matching = 0
        totalvalues = 0
        my_gutenberg_collector = gutenberg_collector.GutenbergCollector()
        my_gutenberg_collector.get_content_at_specific_indexes(1, 200)
        non_matches = []

        text_story_cleaner = clean_text_story.TextStoryCleaner()
        for gutenberg_file in os.listdir(os.getcwd() + "\\documents_downloaded"):
            totalvalues += 1
            download_file_path = 'documents_downloaded/' + gutenberg_file
            opened_file = open(download_file_path, "r", encoding="utf8")
            print("gutenberg file:" + gutenberg_file)
            file_contents = opened_file.read()
            opened_file.close()
            file_meta_cleaned = text_story_cleaner.meta_cleanup(file_contents)
            file_meta_cleaned = ''.join(file_meta_cleaned)
            #print("FILE META")
            #print(file_meta_cleaned)
            #print("OPENEDCONTENTS")
            #print(file_contents)

            if file_meta_cleaned == file_contents:
                #this means that the cleanup DID NOT HAPPEN
                non_matching += 1
                non_matches.append(gutenberg_file)
                output_filepath = 'test_outputs/' + gutenberg_file + '.gutenbergmetaclean'
                opened_output = open(output_filepath, 'w')
                opened_output.write(file_meta_cleaned)
                opened_output.close()




        print("Found [" + str(non_matching) + "] documents that could not be cleaned out of [" + str(totalvalues) + "] total documents checked")
        print("These did not follow matching format:" + str(sorted(non_matches)))






if __name__ == '__main__':
    unittest.main()
    #MyTestCase.test_something()
    #MyTestCase.test_adept_reader()
