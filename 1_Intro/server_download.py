import flask
import os

# Creating the Flask Application.
# The __name__ argument is a special variable in Python that refers to the name of the current module
app=flask.Flask(__name__)

# Defining the Route and Handler:
@app.route("/")
def index():
    if "fileName" not in flask.request.values:
        return "pic.jpeg"
    else:
        data = b""
        try:
            fileName = flask.request.values.get("fileName")
            if fileName !="" and os.path.exists(fileName):
                fobj = open(fileName, "rb")
                data = fobj.read()
                fobj.close()
        except Exception as err:
            data = str(err).encode()
        return data

if __name__=="__main__":(
    # 执行后就启动了一个Web服务器，它的默认地址是http: // 127.0.0.1:5000
    app.run())