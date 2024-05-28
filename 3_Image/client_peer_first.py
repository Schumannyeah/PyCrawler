import urllib.request

from bs4 import BeautifulSoup

# 其中enter是入列函数、fetch是出列函数、empty判断列是否为空。
# 采用Queue类后可以设计广度优先的顺序爬取数据的客户端程序的思想如下：
# ①第一个url入列；
# ②如果列空程序结束，如不为空出列一个url，爬取它的<h3>标题值；
# ③获取url站点的所有超级链接<a>的href值，组成链接列表links，把这些链接全部入栈；
# ④回到②
class Queue:
    def __init__(self):
        self.st=[]

    def fetch(self):
        return self.st.pop(0)

    def enter(self,obj):
        self.st.append(obj)

    def empty(self):
        return len(self.st)==0


def spider(url):
    queue=Queue()
    queue.enter(url)
    while not queue.empty():
        url=queue.fetch()
        try:
            data = urllib.request.urlopen(url)
            data = data.read()
            data = data.decode()
            soup = BeautifulSoup(data, "lxml")
            print(soup.find("h3").text)
            links = soup.select("a")
            for link in links:
                href = link["href"]
                url = start_url + "/" + href
                queue.enter(url)
        except Exception as err:
            print(err)


start_url = "http://127.0.0.1:5000"
spider(start_url)
print("The End")
