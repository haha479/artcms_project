# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField

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


"""
发布文章表单:
1. 标题
2. 分类
3. 封面
4. 内容
5. 发布文章按钮
"""


class ArtForm(FlaskForm):
    title = StringField(
        label='标题',
        validators=[],
        description='标题',
        render_kw={
            'class': 'form-control',
            'placeholder': '输入标题'
        }
    )

    cate = SelectField(
        label='分类',
        validators=[],
        description='分类',
        choices=[(1, '科技'), (2, '搞笑'), (3, '军事')],
        default=3,
        coerce=int,
        render_kw={
            'class': 'form-control'
        }

    )

    logo = FileField(
        label='封面',
        validators=[],
        description='封面',
        render_kw={
            'class': 'form-control-file'
        }

    )

    content = TextAreaField(
        label='内容',
        validators=[],
        description='内容',
        render_kw={
            'style': 'height:300px;',
            'id': 'content'
        }
    )

    submit = SubmitField(
        '发布文章',
        render_kw={
            'class': 'btn btn-primary'
        }
    )
