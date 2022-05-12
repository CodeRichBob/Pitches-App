from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 



app = Flask(__name__)
app.config['SECRET_KEY'] = '3a3b404948c4e3801e8a2a76859c4658'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from pitchapp import routes