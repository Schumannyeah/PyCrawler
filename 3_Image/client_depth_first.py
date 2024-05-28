import urllib.request

from bs4 import BeautifulSoup


class Stack:
    def __init__(self):
        self.st = []

    def pop(self):
        return self.st.pop()

    def push(self, obj):
        self.st.append(obj)

    def empty(self):
        return len(self.st) == 0

# 其中push是压栈函数、pop是出栈函数、empty判断栈是否为空。
# 采用Stack类后可以设计深度优先的顺序爬取数据的客户端程序的思想如下：
# ①第一个url入栈；
# ②如果栈为空程序结束，如不为空出栈一个url，爬取它的<h3>标题值；
# ③获取url站点的所有超级链接<a>的href值，组成链接列表links，把这些链接全部压栈；
# ④回到②
def spider(url):
    stack=Stack()
    stack.push(url)
    while not stack.empty():
        url=stack.pop()
        try:
            data=urllib.request.urlopen(url)
            data=data.read()
            data=data.decode()
            soup=BeautifulSoup(data,"lxml")
            print(soup.find("h3").text)
            links = soup.select("a")
            for i in range(len(links) - 1, -1, -1):
                href = links[i]["href"]
                url = start_url + "/" + href
                stack.push(url)
        except Exception as err:
            print(err)

start_url = "http://127.0.0.1:5000"
spider(start_url)
print("The End")
