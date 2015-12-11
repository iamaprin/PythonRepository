import requests

baseurl = 'http://www.panda.tv/'
room = '31131'
url = baseurl + room
response = requests.request('get', url)
print(response.status_code)
print(response.encoding)
response.encoding = 'unicode'
print(response.text)
