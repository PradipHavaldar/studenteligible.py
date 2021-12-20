from flask import Flask   # WEB FRAMEWOrk
import time
from flask_sqlalchemy import SQLAlchemy #ORM -- OBJECT RELATIONAL MAPPING
app = Flask(__name__)  #FLASK
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # next t
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/ormdb1'  #DATABASE CONFIGURATION
db = SQLAlchemy(app)  #flask and pymysql and sqlalchemy -- integration.


class Student(db.Model):
    id = db.Column('std_id', db.Integer, primary_key=True)
    name = db.Column('emp_name', db.String(40))
    email = db.Column('emp_email', db.String(40),unique=True)
    depat_id = db.Column('emp_deptid', db.String(40))

class Department(db.Model):
    code = db.Column('dept_id', db.Integer, primary_key=True)
    name = db.Column('dept_name', db.String(40))

db.create_all()

#s1 = Student(id=101,name='ABCD',email='abc@gmail.com',depat_id='ETC')
s2 = Student(id=102,name='ABCD1',email='bc@gmail.com',depat_id='ETC')
s3 = Student(id=103,name='ABCD2',email='ac@gmail.com',depat_id='ETC')
s4 = Student(id=104,name='ABCD3',email='ab@gmail.com',depat_id='ETC')

db.session.add_all([s2,s3,s4])
db.session.commit()
