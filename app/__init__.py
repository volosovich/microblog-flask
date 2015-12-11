#initialize project
import os
from flask import Flask #import class Flask
from flask.ext.sqlalchemy import SQLAlchemy #import sql
from flask_login import LoginManager
from flask.ext.openid import OpenID
from config import basedir


app = Flask(__name__) # name of our app
app.config.from_object('config') # add all content from file like object config from app/config.py
db = SQLAlchemy(app) #inicialization db in project
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'

from app import views, models # import views.py and maybee models.py

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 1000)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')
