import urllib.request

from bs4 import BeautifulSoup

# 程序在使用深度优先遍历这棵树，实际上这种递归程序都是采用深度优先的方法遍历树。
def spider(url):
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
            # print(url)
            spider(url)
    except Exception as err:
        print(err)


start_url = "http://127.0.0.1:5000"
spider(start_url)
print("The End")
