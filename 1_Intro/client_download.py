# first run server_get.py then run client_get.py to see the result

import urllib.parse
import urllib.request

url="http://127.0.0.1:5000"

try:
    html = urllib.request.urlopen(url)
    html = html.read()
    fileName = html.decode()
    print("Preparing for downloading:"+fileName)
    data = urllib.request.urlopen(url+"?fileName="+urllib.parse.quote(fileName))
    data = data.read()

    fobj = open("Download_"+fileName,"wb")
    fobj.write(data)
    fobj.close()
    print("Downloading completed:",len(data),"bytes")
except Exception as err:
    print(err)