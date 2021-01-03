from flask import Flask, render_template

app = Flask(__name__)

# 路由解析，通过用户访问路径调用相应函数
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("about_us.html")

@app.route('/learnmore')
def learnmore():
    return render_template("learnmore.html")

@app.route('/attribute')
def attribute():
    return render_template("attribute.html")

@app.route('/bar')
def bar():
    return render_template("bar.html")

@app.route('/geo')
def geo():
    return render_template("geo.html")

@app.route('/liquid')
def liquid():
    return render_template("liquid.html")

@app.route('/pie')
def pie():
    return render_template("pie.html")


if __name__ == '__main__':
    app.run()  # 启动服务器
