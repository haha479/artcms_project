# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

"""
登录表单:
1. 账号
2. 密码
3. 登录按钮

"""


class LoginForm(FlaskForm):
    name = StringField(
        label='账号',
        validators=[],
        description='账号',
        render_kw={
            'class': "form-control",
            'placeholder': "输入账号"
        }

    )

    pwd = PasswordField(
        label='密码',
        validators=[],
        description='密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '输入密码'
        }

    )

    submit = SubmitField(
        '登录',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


"""
1. 账号
2. 密码
3. 确认密码
4. 验证码
5. 注册按钮
"""


class RegisterForm(FlaskForm):
    name = StringField(
        label='账号',
        validators=[],
        description='账号',
        render_kw={
            'class': 'form-control'
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[],
        description='密码',
        render_kw={
            'class': 'form-control'
        }
    )
    repwd = PasswordField(
        label='密码',
        validators=[],
        description='密码',
        render_kw={
            'class': 'form-control'
        }
    )
    code = StringField(
        label='验证码',
        validators=[],
        description='验证码',
        render_kw={
            'class': 'form-control',
            'placeholder': '输入验证码'
        }
    )

    submit = SubmitField(
        '注册',
        render_kw={
            'class': 'btn btn-success'
        }
    )
