from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql//root:1234@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#django --> 8000        --
#flask --> 5000
#pymysql --> API --> application programming interface ..
#http://localhost:5000/  --> which machine and it's port
        # /webapp/welcome --> specific method


@app.route('/configweb/welcome')          #http://localhost:5000/webapp/welcome                       http://127.0.0.1
def welcome_page():
    return 'Welcome to python web application'      # processing on same machine





if __name__ == '__main__':
    #ans  = welcome_page()           #caller
    #print(ans)
    app.run(debug=True)