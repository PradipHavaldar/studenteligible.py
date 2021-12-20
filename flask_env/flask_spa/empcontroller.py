from config import *
from flask import Flask,request,render_template
from models import Employee

def validate_form_data(formdata):
    age = formdata.get('age')
    if not age or not age.isnumeric() or int(age)<=0:
        return "Invalid Age Entered "

@app.route("/index")
def welcome_page():
    return render_template('employee.html',emp = Employee.dummy_employee_instance(),emplist = Employee.query.all())

@app.route("/emp/persist",methods=['POST','GET'])
def save_or_update_emp():
    message = ''
    if request.method=='POST':
        formdata = request.form
        eid = formdata.get('eid')
        dbemp = Employee.query.filter_by(id=eid).first()
        empform = Employee(firstname=formdata.get('firstname'),
                 lastname=formdata.get('lastname'),
                 age=formdata.get('age'),
                 salary=formdata.get('salary'),
                 role=formdata.get('role'),
                 gender=formdata.get('gender'),
                 skills=str(formdata.getlist('skills')),
                 address=formdata.get('address'),
                 contact=formdata.get('contact'),
                 email=formdata.get('email'),
                 domain=str(formdata.getlist('project')))
        error = validate_form_data(formdata)
        if error:
            return render_template('employee.html',
                                   emp=empform,
                                   ageerror=error)
        if dbemp:
            dbemp.firstname = formdata.get('firstname')
            dbemp.lastname = formdata.get('lastname')
            dbemp.age = formdata.get('age')
            dbemp.email = formdata.get('email')
            dbemp.salary = formdata.get('salary')
            dbemp.role = formdata.get('role')
            dbemp.contact = formdata.get('contact')
            dbemp.gender = formdata.get('gender')
            dbemp.address = formdata.get('address')
            dbemp.skills = str(formdata.getlist('skills'))        #m
            dbemp.domain = str(formdata.getlist('project'))        #m
            db.session.commit()
            message = "Employee Record Updated...!"
        else:
            emp = empform
            db.session.add(emp)
            db.session.commit()
            message = "Employee Record Added...!"
    return render_template('employee.html',
                           emp=Employee.dummy_employee_instance(),
                           result = message,
                           emplist = Employee.query.all())

@app.route("/edit/<int:eid>")
def edit_employee(eid):
    dbemp = Employee.query.filter_by(id=eid).first()
    return render_template('employee.html',
                           emp=dbemp,
                           emplist=Employee.query.all())

@app.route("/delete/<int:eid>")
def delete_employee(eid):
    dbemp = Employee.query.filter_by(id=eid).first()
    if dbemp:
        db.session.delete(dbemp)
        db.session.commit()

    return render_template('employee.html',
                           emp=Employee.dummy_employee_instance(),
                           result="",
                           emplist=Employee.query.all())


if __name__ == '__main__':
    app.run(debug=True)