import requests
from lxml import html
url='http://www.tuoshuiba.com/p/5739c443ad82ea0618000ffc/page/1' #需要爬数据的网址
page=requests.Session().get(url) 
tree=html.fromstring(page.text) 
result=tree.xpath('//div[@class="font_big"]/text()') #获取需要的数据
print(result)
