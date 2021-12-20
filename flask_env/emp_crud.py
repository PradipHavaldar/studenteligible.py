from flask import Flask,render_template,request

app = Flask(__name__)       #http://localhost:5000
#app.template_folder = "pages"

@app.route('/emp_crud/welcome/')  #http://localhost:5000/emp/welcome/    ---> employee.html page
def welcome_page():
   #return "welcome to employee crud operation"
   return render_template('employee.html')

@app.route('/emp/add/',methods = ['POST',"GET"])
def add_new_employee():
    print('form submmited...')
    print('POST METHOD',request.form)     # request madhe submit zalela form --> POST method asel tr
    print('GET METHOD ',request.args)     # request method type --> get asel
    nm = request.form.get('enm')
    age = request.form.get('eage')
    skills = request.form.getlist('skill')      #
    print('EMPLOYEE NAME : ',nm)
    print('EMPLOYEE AGE : ', age)
    print('EMPLOYEE SKILLS : ', skills)

    return render_template('employee.html',message = "Data Successfully Submitted...")

@app.route('/emp/update/')
def update_employee():
    pass

@app.route('/emp/search/all/')
def get_all_employees():
    pass

@app.route('/emp/search/')
def search_employees():
    pass

@app.route('/emp/delete/')
def delete_employee():
    pass


if __name__ == '__main__':
    app.run(debug=True)

#https://www.tutorialspoint.com/flask/flask_routing.htm


#flask _ python _ sqlalchemy --> database

    #application running -- if i am making a changes --> Runtime la reflect