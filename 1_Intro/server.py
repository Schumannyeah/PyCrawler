import flask

# Creating the Flask Application.
# The __name__ argument is a special variable in Python that refers to the name of the current module
app=flask.Flask(__name__)

# Defining the Route and Handler:
@app.route("/")
def index():
    try:
        # open the index.html file in binary mode (rb).
        fobj=open("index.html","rb")
        data=fobj.read()
        fobj.close()
        # return the data as response to user's request
        return data
    except Exception as err:
        return str(err)

if __name__=="__main__":(
    # 执行后就启动了一个Web服务器，它的默认地址是http: // 127.0.0.1:5000
    app.run())