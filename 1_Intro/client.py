import urllib.request

url="http://127.0.0.1:5000"
html=urllib.request.urlopen(url)
html=html.read()
# decode using default UTF-8, if others, use html.decode("gbk") for instance
html=html.decode()
print(html)