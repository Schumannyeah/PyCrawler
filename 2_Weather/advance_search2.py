from bs4 import BeautifulSoup

doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
<a href="http://example.com/tilcie">Tilcie</a>
</body>
</html>
'''


def endsWith(s, t):
    if len(s) >= len(t):
        return s[len(s) - len(t):] == t
    return False


def myFilter(tag):
    return (tag.name == "a" and endsWith(tag.text, "cie"))


soup = BeautifulSoup(doc, "lxml")
tags = soup.find_all(myFilter)
for tag in tags:
    print(tag)
