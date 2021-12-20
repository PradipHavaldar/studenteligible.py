from flask_environment_practice.config.dbconfig import db

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

emp_roles = db.Table(
    "emp_roles",
    db.Column('eid',db.ForeignKey("employee.emp_id"),unique=False),
    db.Column('rid',db.ForeignKey("roles.id"),unique=False))

emp_skills=db.Table(
    "emp_skills",
    db.Column('eid',db.ForeignKey("employee.emp_id"),unique=False),
    db.Column('sid',db.ForeignKey("skills.id"),unique=False))

class Employee(db.Model):

    #__tablename__ ='EMPLOYEE_MASTER'
    id=db.Column('emp_id',db.Integer,primary_key=True)
    name=db.Column('emp_name',db.String(30),nullable=False)
    email=db.Column('emp_email',db.String(30),unique=True)
    gender=db.Column('emp_gender',db.String(10))
    active=db.Column('active',db.String(10),default='Y')
    loginref=db.relationship('Login',backref='empref',uselist=False,lazy=False) #backref login mdhin ref  1--1
    roles=db.relationship('Roles',secondary=emp_roles,backref=db.backref("emprefs",lazy=True))#m---m
    address = db.relationship('Address', backref='empref', uselist=True, lazy=True)



#1--1 relation
class Login(db.Model):
    username = db.Column('username', db.String(30), primary_key=True)
    password = db.Column('password', db.String(30))
    empid=db.Column('emp_id',db.ForeignKey("employee.emp_id"),unique=True)
 # login varun empid bhetel pan  employee detail nahi record nhi bhetnar so add loginref in employee



#emp to add actual many to many but here we take as 1--M
class Address(db.Model):

   id=db.Column('id',db.Integer,primary_key=True)
   city=db.Column('city',db.String(30))
   state=db.Column('state',db.String(30))
   pincode=db.Column('pincode',db.Integer)
   active = db.Column('active', db.String(10), default='Y')
   empid = db.Column('emp_id', db.ForeignKey("employee.emp_id"), unique=False)



#m---m
class Skills(db.Model):
        id =db.Column('id',db.Integer,primary_key=True)
        skill=db.Column('skill',db.String(30),)
        active=db.Column('active',db.String(10),default='Y')
        empref= db.relationship('Employee', secondary=emp_skills, backref=db.backref("skills", lazy=True))  # m---m


#M----M relation role -employee

class Roles(db.Model):

        id=db.Column('id',db.Integer,primary_key=True)
        role=db.Column('role',db.String(30))
        active = db.Column('active', db.String(10), default='Y')


db.create_all()

'''
emp--login 1---1
emp--skill m--m
emp --addree 1--m
emp --roles m--m
'''