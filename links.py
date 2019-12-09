import re

f = open('results.txt','r')
data = f.readlines()
text = """The link of this question: https://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string
Also there are some urls: www.google.com, facebook.com, http://test.com/method?param=wasd
The code below catches all urls in text and returns urls in list."""

urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', text)
print(urls)