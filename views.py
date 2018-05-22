# coding:utf8
import os
import datetime
from flask import Flask, render_template, redirect, flash, session, Response
from forms import LoginForm, RegisterForm, ArtForm
from models import User, db
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"


# 登录
@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title="登录", form=form)


# 注册
@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # 通过表单提交过来进行验证
    if form.validate_on_submit():
        # 获取提交的数据
        data = form.data
        # 保存数据到数据库
        user = User(
            name=data['name'],
            pwd=generate_password_hash(data['pwd']),
            addtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        # 提交会话(数据修改)
        # db.session.add(user)
        # db.session.commit()
        # 定义一个闪现
        flash('注册成功, 请登录', 'ok')
        return redirect('/login/')
    else:
        flash('输入正确信息注册', 'err')
    return render_template("register.html", title="注册", form=form)


# 退出登录(302跳转到登录页面)
@app.route("/logout/", methods=['GET'])
def logout():
    return redirect('/login/')


# 发布文章
@app.route("/art/add/", methods=['GET', 'POST'])
def art_add():
    form = ArtForm()
    return render_template("art_add.html", title="发布文章", form=form)


# 编辑文章
@app.route("/art/edit/<int:id>/", methods=['GET', 'POST'])
def art_edit(id):
    return render_template('art_edit.html')


# 删除文章
@app.route('/art/del/<int:id>/', methods=['GET', 'POST'])
def art_del(id):
    return redirect('/art/list/')


# 文章列表
@app.route('/art/list/', methods=['GET', 'POST'])
def art_list():
    return render_template('art_list.html', title="文章列表")

# 验证码
@app.route('/codes/', methods=['GET'])
def codes():
    from codes import Codes
    c = Codes()
    # 获取在Codes中返回的图片信息, (图片名称, 验证码字符)
    info = c.create_code()
    # 获取图片路径
    image = os.path.join(os.path.dirname(__file__), 'static/code') + "/" + info['img_name']

    f = open(image, 'rb')
    image = f.read()

    # 将验证码中的字符存入到session中
    session['code'] = info['code']
    # 在网页中返回验证码图片, jpeg格式
    return Response(image, mimetype='jpeg')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
