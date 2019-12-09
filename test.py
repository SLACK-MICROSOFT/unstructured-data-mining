import requests
from parsel import Selector

import time
start = time.time()
url = 'https://en.wikipedia.org/wiki/Mobile_payment'
response = requests.get(url)

selector = Selector(response.text)

content = selector.xpath('//p').getall()