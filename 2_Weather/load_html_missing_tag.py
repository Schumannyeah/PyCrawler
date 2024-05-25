from bs4 import BeautifulSoup

doc='''
<title>有缺失元素的HTML文档</title>
<div>
<A href='one.html'>one</a>
<p>
<a href='two.html'>two</a>
</DIV>
'''

soup = BeautifulSoup(doc,"lxml")
s = soup.prettify()
print(s)