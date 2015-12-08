import re
import requests


def get_ip():
    url = 'http://www.whereismyip.com/'
    result = requests.get(url)
    text = result.text

    pattern = '([0-9]{0,3}\.){3}[0-9]{0,3}'  # 不能准确匹配ip
    m = re.search(pattern, text)
    ip = m.group(0)
    return ip
