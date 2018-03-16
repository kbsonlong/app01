# coding: utf8
from flask import Flask

from flask_mongoengine import MongoEngine

####################
#  数据库路径等相关配置选项
####################
class Config(object):
    MONGODB_SETTINGS = {

        'db': 'the_way_to_flask',

        'host': 'localhost',

        'port': 27017

    }

app = Flask(__name__)
app.config.from_object(Config)

from config import *
from app01 import views

db =  MongoEngine()
