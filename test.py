import requests
import sys
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        #向指定url地址发送get请求
        response = requests.get(url)
        #如果HTTP请求返回了不成功的状态码，Response.raise_for_status()会抛出一个HTTPError异常
        response.raise_for_status()
        response.encoding = "utf-8"
        return response.text
    except:
        return "Something Wrong!"

#遍历“非小号”首页
for index in range(1, 22):
    url = "https://www.feixiaohao.com/list_" + str(index) + ".html"
    htmlText = getHtmlText(url)
    soup = BeautifulSoup(htmlText, "html.parser")
    sys.setrecursionlimit(1000000)#避免递归深度不足报错
    #找到货币列表
    tds = soup.find_all("td")
    #去掉第一行标题栏
    for td in tds:
        print(td.text)
