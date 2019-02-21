import os
# 设置grpc调用走python类型
# os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_logconfig import LogConfig
from flask_marshmallow import Marshmallow
# from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from config import config
from threading import Thread
import logging

app = Flask(__name__)

# db = SQLAlchemy(model_class=Model)
ma = Marshmallow()
basic_auth = BasicAuth(app)

logger = logging.getLogger(__name__)



@app.route('/')
def index():

    context = {
        'username': 'testhello',
        'gender': '男',
        'age': 666666
    }




    return render_template('index.html', **context)


def create_app(config_name):

    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    ma.init_app(app)
    api = Api(app)
    LogConfig(app)
    basic_auth.init_app(app)

    from app.urls import __make_url
    __make_url(api)

    return app
