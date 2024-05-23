import os

from flask import Flask

# Creating the Flask Application.
# The __name__ argument is a special variable in Python that refers to the name of the current module
app = Flask(__name__)


# Defining the Route and Handler:
@app.route("/")
def show():
    if os.path.exists("students.txt"):
        st = "<h3>学生信息表</h3>"
        st = st + "<table border='1'width='300'>"
        fobj = open("students.txt", "rt", encoding="utf-8")
        while True:
            # 读取一行，去除行尾部"\n"换行符号
            s = fobj.readline().strip("\n")
            # 如果读到文件尾部就退出
            if s == "":
                break
            # 按逗号拆分开
            s = s.split(",")
            st = st + "<tr>"
            # 把各个数据组织在<td>...</td>的单元中
            for i in range(len(s)):
                st = st + "<td>" + s[i] + "</td>"
                # 完成一行
                st = st + "</tr>"
            fobj.close()
            st = st + "</table>"
            return st


if __name__ == "__main__": (
    # 执行后就启动了一个Web服务器，它的默认地址是http: // 127.0.0.1:5000
    app.run())
