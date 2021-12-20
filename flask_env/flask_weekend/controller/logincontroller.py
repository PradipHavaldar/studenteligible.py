from flask_environment_practice.config.dbconfig import app,db
from flask_environment_practice.model.model import Login
from flask import request,render_template,request_started,request_finished


@app.route('/username')
def enter_username():
    if request.method=='POSt':
            formdata=request.form
            username=formdata.get('username')
            password=formdata.get('password')

    render_template('login.html')
    pass

def enter_password():
    pass