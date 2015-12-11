import requests
from monitor.test import MyHTMLParser


url = 'http://www.panda.tv/search'
key = '周二珂'
args = {'key': key}
header = {'user-agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:42.0) Gecko/20100101 Firefox/42.0"'}
# response = requests.request('get', url, params=args, headers=header)
# print(response.status_code)
# print(response.text)
# parser = MyHTMLParser()
# parser.feed(response.text)

cookie = {'cookies': '"__guid=96554777.4116491961764843500.1449752660757.6753; '
                     'monitor_count=5; '
                     'Hm_lvt_204071a8b1d0b2a04c782c44b88eb996=1449752661;'
                     'Hm_lpvt_204071a8b1d0b2a04c782c44b88eb996=1449752773"'}
response = requests.request('get', url, params=args, headers=header, cookies=cookie)
print(response.cookies.values())
print(response.headers)
parser = MyHTMLParser()
parser.feed(response.text)
