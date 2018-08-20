import threading
from Machines import adept_reader
from os import path
import os
import random
from Collectors import gutenberg_collector
from Cleaners import clean_text_story
from Creators import create_text_story
import time

class AdeptReaderRunner:

    def __init__(self):
        #download gutenberg content
        #set up an adept reader based on parameters
        #have it read through things and then intermitently output files with created output

        adept_reader_non_lossy = adept_reader.AdeptReader(0.0)
        adept_reader_slightly_lossy = adept_reader.AdeptReader(0.02)
        adept_reader_semi_lossy = adept_reader.AdeptReader(0.05)
        self.adept_readers = [adept_reader_non_lossy, adept_reader_semi_lossy, adept_reader_slightly_lossy]
        self.texts = []
        self.cleaner = clean_text_story.TextStoryCleaner()
        self.creator = create_text_story.TextStoryCreator()


    def begin_experiment(self):
        threads = []
        #need to pick a randomized collection of texts
        self.select_texts()
        indexvalue = 1
        runsperfile = 2
        self.setup_directory()
        for ar in self.adept_readers:
            t = threading.Thread(target=self.run_one_experiment, args=(ar, indexvalue, runsperfile, "LossinessIs" + str(ar.lossiness)))
            indexvalue = indexvalue + 1
            threads.append(t)
            t.start()

    def select_texts(self):
        gc = gutenberg_collector.GutenbergCollector()
        gc.get_content_at_indexes()
        allfiles = []
        for filename in os.listdir(os.getcwd() + "\\documents_downloaded"):
            if '.txt' in filename:
                allfiles.append(filename)
        self.texts = random.sample(set(allfiles), 20)


    def setup_directory(self):
        basepath = path.dirname(__file__)
        dirpath = path.abspath(path.join(basepath, "..", 'experiment_outputs/'))
        if not path.exists(dirpath):
            os.mkdir(dirpath)


    def setup_experiment_directory(self, experiment_name):
        basepath = path.dirname(__file__)
        dirpath = path.abspath(path.join(basepath, "..", 'experiment_outputs/' + str(experiment_name) + '/'))
        if not path.exists(dirpath):
            os.mkdir(dirpath)
        else:
            for the_file in os.listdir(dirpath):
                try:
                    file_path = os.path.join(dirpath, the_file)
                    os.unlink(file_path)
                except Exception as e:
                    print(e)


    def run_one_experiment(self, adept_reader_config, indexvalue, runs, experiment_name):
        self.setup_experiment_directory(experiment_name)
        incre_number = 1
        for file_name in self.texts:
            basepath = path.dirname(__file__)
            filepath = path.abspath(path.join(basepath, "..", 'documents_downloaded/' + file_name))
            cleaned_text = self.cleaner.clean_text_story(filepath)
            for x in range(runs):
                adept_reader_config.add_to_memory_lossy_consolidation(cleaned_text)
            writeoutputfilepath = path.abspath(path.join(basepath, "..", 'experiment_outputs/' + str(experiment_name) + '/' + str(incre_number) + "-" + file_name))
            opened_file = open(writeoutputfilepath, 'w')
            opened_file.write(self.creator.create_text_story(adept_reader_config.memory, 500))
            opened_file.close()
            incre_number = incre_number + 1



    #def reading_loop(self):

class ReaderRunnerThread(threading.Thread):

    def __init__(self):
        pass