from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.template_folder = "pages/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/db1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)