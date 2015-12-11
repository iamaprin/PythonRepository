import requests
from monitor.test import MyHTMLParser

data = requests.get('http://www.panda.tv/35723')
# print(data.text)
parse = MyHTMLParser()
parse.feed(data.text)

