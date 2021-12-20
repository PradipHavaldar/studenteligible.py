from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/demo/good/')


def good():
    return "good good good"



if __name__ == '__main__':
    app.run(debug=True)