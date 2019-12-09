import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize import PunktSentenceTokenizer



import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def getTitle(link):
    """Attempt to get a title."""
    title = ''
    if link.title.string is not None:
        title = link.title.string
    elif link.find("h1") is not None:
        title = link.find("h1")
    return title


def getDescription(link):
    """Attempt to get description."""
    ''' Returning on the basis of text present in p only'''
    return link.find_all('p')


def getImage(link):
    """Attempt to get image."""
    image = ''
    if link.find("meta", property="og:image") is not None:
        image = link.find("meta", property="og:image").get('content')
    elif link.find("img") is not None:
        image = link.find("img").get('href')
    return image


def getSiteName(link, url):
    """Attempt to get the site's base name."""
    sitename = ''
    if link.find("meta", property="og:site_name") is not None:
        sitename = link.find("meta", property="og:site_name").get('content')
    else:
        sitename = url.split('//')[1]
        name = sitename.split('/')[0]
        name = sitename.rsplit('.')[1]
        return name.capitalize()
    return sitename



# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = 'https://en.wikipedia.org/wiki/Mobile_payment'
url = 'https://business.paytm.com/'
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
p= getDescription(soup)
p =[str(i) for i in p]
p = " ".join(p)

s = striphtml(p)
sentences = sent_tokenize(s)
# w = word_tokenize(sentences[0])
def nltk_NER(sentences):
    custom_sent_tokenizer = PunktSentenceTokenizer()
    for i in range(len(sentences)):
        tokenized = custom_sent_tokenizer.tokenize(sentences[i])
        for i in tokenized:
            print(i)
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
from nltk.tag.stanford import StanfordNERTagger

def stanfordNER(sentences):
    st = StanfordNERTagger('/home/aaquib/ir-project/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz','/home/aaquib/ir-project/stanford-ner-2018-10-16/stanford-ner.jar')
    print (st.tag(' i payed the amount by paytm and google pay'.split()))

    # for i in range(len(sentences)):
    #     tokenized = custom_sent_tokenizer.tokenize(sentences[i])
    #     print(tokenized)
    #     print(st.tag(tokenized.split()))

    a = st.tag(sentences[0].split())




import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from pprint import pprint

nlp = en_core_web_sm.load()

def spaceNER(sentences):
    for   i in range(len(sentences)):
        doc = nlp(" ".join(sentences[i].rsplit()))
        pprint([(X.text, X.label_) for X in doc.ents])