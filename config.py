import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'MYSQL+PYMYSQL://root:root@localhost:3306/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
