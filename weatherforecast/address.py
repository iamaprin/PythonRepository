import requests
from weatherforecast import ip


def get_address_city():
    ipaddr = ip.get_ip()
    print(ipaddr)
    apikey = '09d2369dd5b6b39d1b4c3a49b9d71e6e'  # no secret
    baseurl = 'http://apis.baidu.com/apistore/iplookupservice/iplookup'

    payload = {'ip': ipaddr}
    header = {'apikey': apikey}
    result = requests.request('get', baseurl, params=payload, headers=header)

    if result.status_code == 200:
        jsondata = result.json()
        s = jsondata['retData']['city']
    else:
        s = 'error'

    return s
