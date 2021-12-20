from flask_env.flask_weekend.config.dbconfig import db




emp_roles=db.Table(
     "emp_roles",
        db.Column('eid',db.ForeignKey("employee.emp_id"),unique=False),
        db.Column('rid',db.ForeignKey("roles.id"),unique=False),

)


emp_skill=db.Table (
      "emp_skill",
        db.Column('eid',db.ForeignKey("employee.emp_id"),unique=False),
        db.Column('sid',db.ForeignKey("skill.id"),unique=False)
            )



class Employee(db.Model):

    id=db.Column('emp_id',db.Integer,primary_key=True)
    name = db.Column('emp_name', db.String(30),nullable=False)
    email = db.Column('emp_email', db.String(30), unique=True)
    gender = db.Column('emp_gender', db.String(10))
    salary=db.Column('emp_salary',db.Float())
    active=db.Column('active',db.String(10),default='Y')
    loginref=db.relationship('login',backref='empref',uselist=False,lazy=False)
    roles=db.relationship('Roles',secondary=emp_roles,backref=db.backref("emprefs",lazy=True))
    Addresses = db.relationship('Address', backref='empref', uselist=True, lazy=True,cascade='all, delete')


class Address(db.Model):

     id = db.Column('id', db.Integer, primary_key=True)
     city = db.Column('city', db.String(30) )
     state = db.Column('state', db.String(30))
     pincode = db.Column('pincode', db.Integer())
     active = db.Column('active', db.String(10), default='Y')
     empref = db.Column('emp_id', db.ForeignKey("employee.emp_id"), unique=False, nullable=False)


class Skill(db.Model):

    id = db.Column('id', db.Integer,primary_key=True)
    skill = db.Column('skill', db.String(30))
    active = db.Column('active', db.String(10), default='Y')
    emprefs = db.relationship('Employee', secondary=emp_skill, backref=db.backref("skills", lazy=True))

class Roles(db.Model):



    id = db.Column('id', db.Integer,primary_key=True)
    role = db.Column('role', db.String(30))
    active = db.Column('active', db.String(10), default='Y')


class Login(db.Model):


    username = db.Column('username',db.String(30),primary_key=True)
    password = db.Column('password',db.String(30))
    empid=db.Column('emp_id',db.ForeignKey("employee.emp_id"),unique=True,nullable=False)


db.create_all()

