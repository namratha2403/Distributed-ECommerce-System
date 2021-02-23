from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
import time
import csv

from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY']='djshakuo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"




def start_timer():
    start_time = start_time = time.time()
    return start_time


def stop_timer(start_time, funct):
    # output is in seconds
    resp_time = (time.time() - start_time)
    with open(r'/Users/sukanyasaha/Desktop/Distributed Systems/Assignments/Assignment 2/Assignment2-Sukanya/test1/latency_report.csv', 'a', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([funct, str(resp_time)])
    return

from shop.products import routes
from shop.admin import routes
from shop.carts import carts
from shop.customers import routes

from flask import request

