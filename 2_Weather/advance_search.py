from bs4 import BeautifulSoup

doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
</body>
</html>
'''


def myFilter(tag):
    if tag.name == 'a':  # Directly check if the tag is an <a> tag
        if 'href' in tag.attrs and tag['href'] == "http://example.com/lacie":  # Check if 'href' exists and matches
            return True
    return False


soup = BeautifulSoup(doc, "lxml")
tag = soup.find_all(myFilter)
print(tag)
