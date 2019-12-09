from nltk.tag.stanford import StanfordNERTagger
st = StanfordNERTagger('/home/aaquib/ir-project/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz','/home/aaquib/ir-project/stanford-ner-2018-10-16/stanford-ner.jar')
print (st.tag(' Stony Brook University in Bengaluru'.split()))
