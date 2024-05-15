import flask

app=flask.Flask(__name__)

@app.route("/")
def hello():
    return"你好"

@app.route("/hi")
def hi():
    return"Hi,你好"

if __name__=="__main__":(
    # 执行后就启动了一个Web服务器，它的默认地址是http: // 127.0.0.1:5000
    app.run())