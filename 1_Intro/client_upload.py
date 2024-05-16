# first run server_get.py then run client_get.py to see the result

import urllib.request
import os

url="http://127.0.0.1:5000/upload"
fileName=input("Enter the file:")
print(fileName)

if os.path.exists(fileName):
    fobj=open(fileName,"rb")
    data=fobj.read()
    fobj.close()
    p=fileName.rfind("\\")
    fileName=fileName[p+1:]
    print("Ready to upload:"+fileName)
    headers = {'content-type': 'application/octet-stream'}
    purl = url + "?fileName=" + urllib.parse.quote(fileName)
    req = urllib.request.Request(purl, data, headers)
    msg = urllib.request.urlopen(req)
    msg = msg.read().decode()
    if msg == "OK":
        print("Upload successfully:", len(data), "bytes")
    else:
        print(msg)
else:
    print("File doesn't exist.")