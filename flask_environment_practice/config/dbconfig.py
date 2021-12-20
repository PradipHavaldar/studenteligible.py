from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.template_folder = "templates/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/prcflaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

