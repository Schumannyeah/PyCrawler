import flask
import os

# Creating the Flask Application.
# The __name__ argument is a special variable in Python that refers to the name of the current module
app=flask.Flask(__name__)

# Defining the Route and Handler:
@app.route("/upload",methods=["POST"])
def uploadFile():
    msg=""
    try:
        if "fileName" in flask.request.values:
            fileName=flask.request.values.get("fileName")
            data=flask.request.get_data()
            fobj=open("upload_"+fileName,"wb")
            fobj.write(data)
            fobj.close()
            msg="OK"
        else:
            msg="File is not uploaded accordingly"
    except Exception as err:
        print(err)
        msg=str(err)
    return msg

if __name__=="__main__":(
    # 执行后就启动了一个Web服务器，它的默认地址是http: // 127.0.0.1:5000
    app.run())