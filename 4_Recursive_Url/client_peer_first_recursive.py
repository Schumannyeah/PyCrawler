import urllib.request

from bs4 import BeautifulSoup

# 图的广度优先遍历BFS算法是一个分层搜索的过程，和树的层序遍历算法类同，
# 它也需要一个队列以保持遍历过的顶点顺序，以便按出队的顺序再去访问这些顶点的邻接顶点。
# 基本实现思想：
# ①顶点v入队列。
# ②当队列非空时则继续执行，否则算法结束。
# ③出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。
# ④查找顶点v的第一个邻接顶点col。
# ⑤若v的邻接顶点col未被访问过的，则col入队列。
# ⑥继续查找顶点v的另一个新的邻接顶点col，转到步骤⑤。直到顶点v的所有未被访问过的邻接点处理完。转到步骤②。
# 广度优先遍历图是以顶点v为起始点，由近至远，依次访问和v有路径相通而且路径长度为1，2，……的顶点。
# 为了使“先被访问顶点的邻接点”先于“后被访问顶点的邻接点”被访问，需设置队列存储访问的顶点。
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
        if url not in urls:
            try:
                urls.append(url)
                data=urllib.request.urlopen(url)
                data=data.read()
                data=data.decode()
                soup=BeautifulSoup(data,"lxml")
                print(soup.find("h3").text)
                links=soup.select("a")
                for link in links:
                    href = link["href"]
                    url = start_url + "/" + href
                    queue.enter(url)
            except Exception as err:
                print(err)

start_url = "http://127.0.0.1:5000"
urls=[]
spider(start_url)
print("The End")
