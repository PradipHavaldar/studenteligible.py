from flask import Flask   # WEB FRAMEWOrk
import time
from flask_sqlalchemy import SQLAlchemy #ORM -- OBJECT RELATIONAL MAPPING
app = Flask(__name__)  #FLASK
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # next t
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/ormdb'  #DATABASE CONFIGURATION
db = SQLAlchemy(app)  #flask and pymysql and sqlalchemy -- integration.


class Employee(db.Model):  # a class --> which is aware about -- python fields --> mapped with --> database column k sath
    id = db.Column('emp_id',db.Integer,primary_key=True)
    name = db.Column('emp_name', db.String(40))
    age = db.Column('emp_age', db.Integer)
    salary = db.Column('emp_salary', db.Float)
    email = db.Column('emp_email', db.String(40), unique=True)
    role = db.Column('emp_role', db.String(30))

db.create_all()

e1 = Employee(name='XXXX',age=34,salary=31289.23,email='xabc0@gmail.com',role='Lead')

db.session.add(e1)
db.session.commit()





#create table
#table banakar dega --> it's equivalent -- create table employee
#db.create_all()     # FIND OUT ALL THOSE CLASSES --> db.model k child hai  field--column
print('Table created Successfully....')
time.sleep(3)

#insert into
e1 = Employee(id=101,name='ABCD',age=29,salary=1289.23,email='abc@gmail.com',role='SSE')
db.session.add(e1)    # session ack data --> python-- database connection -->
db.session.commit()     # final karana -->
print('Employee one inserted ...')
time.sleep(3)


#bulk insert
e2 = Employee(id=102,name='ABCD1',age=29,salary=41289.23,email='abc2@gmail.com',role='SSE')
e3 = Employee(id=103,name='ABCD2',age=49,salary=13289.23,email='abc3@gmail.com',role='Manager')
e4 = Employee(id=104,name='ABCD3',age=33,salary=51289.23,email='abc4@gmail.com',role='Lead')
db.session.add_all([e2,e3,e4])
db.session.commit()
print('Bulk insert completed...')




'''emps = Employee.query.all()
def mysort_logic(emp):
    return emp.salary
emps.sort(key=mysort_logic,reverse=True) # salary k
print(emps[-2].salary)    # second last'''









