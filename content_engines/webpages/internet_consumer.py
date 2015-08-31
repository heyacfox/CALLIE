from html.parser import HTMLParser
from urllib.parse import urlparse
import urllib.request

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_date(self, data):
        print("Encountered some data :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

mywebinput = urlparse('http://www.heyacfox.net/index.html')

with urllib.request.urlopen('http://www.heyacfox.net') as response:
    html = response.read()

#function to open up a web page, returns an html file as a string
def webpageOpen(someUrl):
    with urllib.request.urlopen(someUrl) as response:
        html = response.read().decode('UTF-8')
        return html

#function to save a web page in a folder
def saveWebpage(name, htmlString, folder):
    path = folder + "/"
    myFile = open(path + name + ".html", 'a')
    myFile.write(htmlString)
    myFile.close()
#functio to find web pages that are links on a certain web page

#We need to be suspicious of links. 
