import requests

from weatherforecast import address


def get_weather():
    district = address.get_address_city()
    print(district)

    baseurl = 'http://apis.baidu.com/showapi_open_bus/weather_showapi/address'
    apikey = '09d2369dd5b6b39d1b4c3a49b9d71e6e'

    payload = {'area': district}
    header = {'apikey': apikey}
    result = requests.request('get', baseurl, params=payload, headers=header)
    # print(result.json())
    jsondata = result.json()
    print('白天天气:', jsondata['showapi_res_body']['f2']['day_weather'])
    print('白天风力:', jsondata['showapi_res_body']['f2']['day_wind_power'])
    print('...')
