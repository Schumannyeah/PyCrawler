import urllib.request

from bs4 import BeautifulSoup

# 深度优先搜索(Depth-FirstSearch)。
# 相应地，用此方法遍历图就很自然地称之为图的深度优先遍历，基本实现思想如下：
# ①访问顶点v；
# ②从v的未被访问的邻接点中选取一个顶点w，从w出发进行深度优先遍历；
# ③重复上述两步，直至图中所有和v有路径相通的顶点都被访问到。
class Stack:
    def __init__(self):
        self.st = []

    def pop(self):
        return self.st.pop()

    def push(self, obj):
        self.st.append(obj)

    def empty(self):
        return len(self.st) == 0


def spider(url):
    global urls
    stack=Stack()
    stack.push(url)
    while not stack.empty():
        url=stack.pop()
        if url not in urls:
            urls.append(url)
            try:
                data=urllib.request.urlopen(url)
                data=data.read()
                data=data.decode()
                soup = BeautifulSoup(data, "lxml")
                print(soup.find("h3").text)
                links = soup.select("a")
                for i in range(len(links) - 1, -1, -1):
                    href = links[i]["href"]
                    url = start_url + "/" + href
                    stack.push(url)
            except Exception as err:
                print(err)

start_url = "http://127.0.0.1:5000"
urls=[]
spider(start_url)
print("The End")
