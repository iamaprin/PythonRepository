### weather forecast
#### names
**package and module names**：short，all-lowercase names
**class names**：CapWords
**function names**： lowercase，with words separated by underscores 
小写，单词之间用下划线分割

<br>
#### steps：
1、获取自己的外网ip。
- 通过`socket`包获取的是内网ip，所以需要通过访问外部网站获取ip，
这里使用的是*http://www.whereismyip.com*。
- 使用`requests`获取网站的内容，再通过`re`获取其中的ip信息。

2、根据ip获取地理位置
- 使用了baidu的api，地址为*http://apis.baidu.com/apistore/iplookupservice/iplookup*。
- 请求的类型为*get*，需要包含apikey和ip，apikey存放在header中，ip存放在请求url中。
- 获取的数据是json类型的，其中有关于地址的详细信息，这里我们只需要**city**的值。

3、根据地理位置获取该城市的天气情况
- 同样使用了外部api，地址为*http://apis.baidu.com/showapi_open_bus/weather_showapi/address*。
- 请求数据方法和步骤二差不多。

<br>
#### note：
安装requests：
1. 获取：<br>`git clone https://github.com/kennethreitz/requests.git`
2. 进入requests文件夹，执行安装<br>`cd ./requests`<br>`python setup.py install`
3. `requests`位置：<br>`python_home\Lib\site-packages\`

<br>
用到的requests的相关方法：
1. `requests.get(url)`
2. `requests.request(method, url, **kwargs)`：返回`requests.Response`对象
3. `requests.Response`：<br>`Response.content`：**bytes**<br>`Response.text`：**unicode**<br>`Response.json`：**json-encoded**
4. `**kwargs`：<br>`params`：查询字符串，**ip**存放位置<br>`headers`：头信息，**apikey**存放位置
5. `Response.json`：可以通过key获取相应的值

<br>
用到的re的相关方法：
1. `re.search(pattern, string)`:按照pattern扫描字符串
2. `re.match(pattern, string)`：在string开始处匹配pattern
3. 返回**match**对象或者**None**

<br>
[weather forecast代码地址](https://github.com/iamaprin/PythonRepository/tree/master/weatherforecast)