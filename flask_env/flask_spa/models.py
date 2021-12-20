#from flask_spa.config import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
  __tablename__ = 'EMPLOYEE_MASTER'

  id = db.Column('emp_id',db.Integer,primary_key=True)
  firstname = db.Column('emp_fname',db.String(30))
  lastname = db.Column('emp_lname', db.String(30))
  age = db.Column('emp_age', db.Integer)
  salary = db.Column('emp_salary', db.Float)
  role = db.Column('emp_role', db.String(1000))
  gender = db.Column('emp_gender', db.String(30))
  skills = db.Column('emp_skills', db.String(100))
  address = db.Column('emp_address', db.String(1025))
  contact = db.Column('emp_contact', db.BigInteger, unique=True)
  email = db.Column('emp_email', db.String(30),unique=True)
  domain = db.Column('emp_domain', db.String(1024))

  @classmethod
  def dummy_employee_instance(cls):
    return Employee(id=0,firstname='',lastname='',age=0,salary=0.0,role='',gender='',skills='',address='',contact=0,email='',domain='')

#db.drop_all()
db.create_all() # this statement will create a table
