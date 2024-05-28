import urllib.request

from bs4 import BeautifulSoup


# 程序在使用深度优先遍历这棵树，实际上这种递归程序都是采用深度优先的方法遍历树。
# 假设给定图G的初态是所有顶点均未曾访问过。在G中任选一顶点v为初始出发点
# （原点），则深度优先遍历可定义如下：首先访问出发点v，并将其标记为已访问；
# 然后依次从v出发搜索v的每个邻接点w。若w未曾访问过，则以w为新的出发点继续进行深度优先遍历，
# 直至图中所有和原点v有路径相通的顶点（亦称为从原点可达的顶点）均已被访问为止。图的深度优先遍历类似于树的前序遍历。

def spider(url):
    global urls
    if url not in urls:
        urls.append(url)
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
                spider(url)
        except Exception as err:
            print(err)


start_url = "http://127.0.0.1:5000"
urls = []
spider(start_url)
print("The End")
