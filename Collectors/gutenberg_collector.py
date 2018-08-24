import urllib.request
import urllib.error
from os import path
import os


class GutenbergCollector:

    def __init__(self):
        self.current_index = 1
        self.pathInitial = 'http://www.gutenberg.org/files/'

    def get_content_from_url(self, url_index):
        if self.already_have_file(url_index):
            print("Already Downloaded:" + str(url_index))
            return
        try:
            true_path = self.pathInitial + str(url_index) + '/' + str(url_index) + '.txt'
            print("Getting Content From:" + true_path)
            open_url = urllib.request.urlopen(true_path)
        except urllib.error.HTTPError:
            try:
                secondary_path = self.pathInitial + str(url_index) + '/' + str(url_index) + '-0.txt'
                print("TruePath failed, now trying:" + secondary_path)
                open_url = urllib.request.urlopen(secondary_path)
            except urllib.error.HTTPError:
                print("No valid Text File Available for:" + str(url_index))
                return

        data = open_url.read()
        try:
            text = data.decode('utf-8')
            print("length of content:" + str(len(text)))
            self.write_to_file(text, url_index)
        except UnicodeDecodeError:
            print("Unable to decode content:" + str(url_index))
            return

    def write_to_file(self, content, url_index):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", 'documents_downloaded/' + str(url_index) + ".txt"))
        text_file = open(filepath, "w", encoding="utf8")
        try:
            text_file.write(content)
            text_file.close()
            #need to check that we can open it as utf8, no invalid characters
            text_file2 = open(filepath, 'r', encoding='utf8')
            text_file2.read()
            text_file2.close()
        except UnicodeEncodeError:
            print("Couldn't write this file due to encoding error:" + str(url_index))
            text_file.close()
            os.unlink(filepath)
        print("File written:" + 'documents_downloaded/' + str(url_index) + ".txt")

    def get_content_at_indexes(self):
        for x in range(1, 201):
            self.get_content_from_url(x)
        #content 37 doesn't follow same format

    def get_content_at_specific_indexes(self, initial, final):
        for x in range(initial, final+1):
            self.get_content_from_url(x)

    def already_have_file(self, url_index):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", 'documents_downloaded/' + str(url_index) + ".txt"))
        if path.isfile(filepath):
            return True
        else:
            return False