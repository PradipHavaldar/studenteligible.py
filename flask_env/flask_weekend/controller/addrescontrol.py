from flask_environment_practice.config.dbconfig import app,db
from flask_environment_practice.model.model import Address
from flask import request,render_template,request_started,request_finished
@app.route("/address")
@app.route("/address/save",methods=['GET','POST'])
def save_or_update():
    message=''
    if request.method=='POST':

        formdata = request.form
        aid=int(formdata.get('aid'))
        adr=Address.query.filter_by(id=aid).first()
        if adr:
            adr.city=formdata.get('city')
            adr.state = formdata.get('state')
            adr.pincode = formdata.get('pincode')

            db.session.commit()
            message="Address Record Updated......."
        else:

            city=formdata.get('city')
            state=formdata.get('state')
            pincode=formdata.get('pincode')
            Address(city=city,state=state,pincode=pincode)

            db.session.add(adr)
            db.session.commit()
            message='Address record save'

    return render_template('address.html',message=message,address=Address(id=0,city='',state='',pincode=0))

@app.route("/address/edit/<int:aid>",methods=['GET'])
def get_addresses(aid):
     return render_template('address.html',address=Address.query.filter_by(id=aid).first())


@app.route("/address/delete/<int:aid>",methods=['GET'])
def delete_address(aid):
    adr=Address.query.filter_by(id=aid).first()
    if adr:
        db.session.detete(adr)
        db.session.commit()
        message='Record deleted Successfully.....!'


    return render_template('address.html',message=message,address=Address(id=0,city='',state='',pincode=0))


if __name__=='__main__':
    app.run(debug=True)