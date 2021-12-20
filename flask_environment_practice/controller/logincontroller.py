from flask_environment_practice.config.dbconfig import app
from flask import request ,render_template
#from flask import Flask, render_template, request
from flask_environment_practice.model.model import *

#http://5000/login  ---->get

@app.route("/",methods=['GET'])
@app.route("/login",methods=['GET','POST'])

def authenticate_user():
    message=f''
    if request.method=='POST':

        formdata=request.form

        if formdata.get('user') or formdata.get('password'):

            username=formdata.get('user')
            password=formdata.get('password')
            login=Login.query.filter_by(username=username).first()
            if login and login.password==password:
                return render_template('home.html')
            else:
                message="Invalid Crendetials"
        else:
            message='Credentials Required'
    return render_template('login.html',message=message)





app.run(debug=True)