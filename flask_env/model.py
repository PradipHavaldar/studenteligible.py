
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flaskdb5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Employee(db.Model):
  __tablename__ = 'EMPLOYEE_MASTER'

  id = db.Column('emp_id',db.Integer,primary_key=True)
  name = db.Column('emp_name',db.String(30))
  age = db.Column('emp_age', db.Integer)
  salary = db.Column('emp_salary', db.Float)
  role = db.Column('emp_role', db.String(30))
  gender = db.Column('emp_gender', db.String(30))
  skills = db.Column('emp_skills', db.String(30))
  city = db.Column('emp_city', db.String(30))
  hobbies = db.Column('emp_hobbies', db.String(30))

#if someone imports --> model --> automatically tables will be created..
db.create_all()

#Employee(id,name,age,salary,role,gender,skills,city,hobbies)

#Note --> one column should not have comma seperate values-->
        #bcoz -- it doesnt follow  1NF --> Normalization