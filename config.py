import os
from sqlalchemy import create_engine


import urllib

class Config(object):
    SECRET_KEY = 'Clave Nueva'
    SESSION_COOKIE_NAME = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Deadmau6@localhost/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False