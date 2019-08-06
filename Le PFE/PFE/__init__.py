from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'e1629760ff816b5f25223835689744dd'
APP.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/myPFE'
DB = SQLAlchemy(APP)
LM = LoginManager(APP)
bcrypt = Bcrypt(APP)
from PFE import route
