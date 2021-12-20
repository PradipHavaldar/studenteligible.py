from flask import render_template,request
from model import Employee,db,app

#app = Flask(__name__)       #http://localhost:5000
#app.template_folder = "pages"

@app.route('/emp/welcome/')  #http://localhost:5000/emp/welcome/    ---> employee.html page
def welcome_page():
   #return "welcome to employee crud operation"
   return render_template('employee.html')

def convert_multi_tostr(values):
    #values = ["A","B","C"]
    finalvalues = ''
    for ind,item in enumerate(values):
        if ind == 0:
            finalvalues = item
        else:
            finalvalues = finalvalues +','+item
   #print(finalvalues)
    return finalvalues
#convert_multi_tostr()



@app.route('/emp/add/',methods = ['POST',"GET"])
def add_new_employee():
    result = ''
    if request.method == 'POST':
         formdata = request.form  #POST method mein
         emp = Employee(id=formdata.get('eid'),
                        name=formdata.get('enm'),
                        age=formdata.get('eage'),
                        salary=formdata.get('esal'),
                        role=formdata.get('erole'),
                        gender=formdata.get('gender'),
                        skills=convert_multi_tostr(formdata.getlist('skill')),  # m
                        city=formdata.get('city'),
                        hobbies=convert_multi_tostr(formdata.getlist('hobbies')))  # m

         eid = formdata.get('eid')
         emprecord = Employee.query.filter_by(id=eid).first()
         if emprecord:
             result = "Duplicate Record"
             #as it is..
             data = emp        #[all the data which entered by enduser]
         else:
             db.session.add(emp)
             db.session.commit()
             result = "Data Successfully Submitted..."
             #form shud be blank
             data = Employee(id=0,
                        name='',
                        age=0,
                        salary=0.0,
                        role='',
                        gender='',
                        skills='',  # m
                        city='',
                        hobbies='')
    return render_template('employee.html',message = result,emp = data)

@app.route('/emp/update/')
def update_employee():
    pass

@app.route('/emp/search/all/')
def get_all_employees():
    return render_template('show.html', emplist = Employee.query.all())

@app.route('/emp/search/')
def search_employees():
    pass

@app.route('/emp/delete/')
def delete_employee():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    #pass

#https://www.tutorialspoint.com/flask/flask_routing.htm


#flask _ python _ sqlalchemy --> database

    #application running -- if i am making a changes --> Runtime la reflect