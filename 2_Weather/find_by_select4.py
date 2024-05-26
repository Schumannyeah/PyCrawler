from bs4 import BeautifulSoup

doc="<body>demo<div>A</div><b>X</b><p>B</p><span><p>C</p></span><p>D</p></div></body>"

# 查找<div>后面的所有同级别的<p>兄弟结点
soup = BeautifulSoup(doc, "lxml")
tags = soup.select("div ~ p")
for tag in tags:
    print(tag)

s = soup.prettify()
print(s)