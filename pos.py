import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


custom_sent_tokenizer = PunktSentenceTokenizer()
f = open('data.txt', 'r')
# sample_text = "Ram is the best boy in the class. Aman is studying in his house today so he is absent"
content = f.readlines()
sample_text = "".join([i.rstrip() for i in content])

tokenized = custom_sent_tokenizer.tokenize(sample_text)
for i in tokenized:
    print(i)
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    # print(tagged)
    namedEnt = nltk.ne_chunk(tagged, binary=True)
    namedEnt.draw()
