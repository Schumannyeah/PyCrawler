from bs4 import BeautifulSoup

doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The<i>Dormouse's</i>story</b>Once upon a time...</p>
</body>
</html>
'''

soup = BeautifulSoup(doc, "lxml")
tag = soup.find("p")
for x in tag.children:
    print(x)
