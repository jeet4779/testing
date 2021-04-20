from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Covid.db'
db = SQLAlchemy(app)

class Donar(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    city = db.Column(db.String(80),nullable=False)
    state = db.Column(db.String(80),nullable=False)
    blood = db.Column(db.String(80),nullable=False)
    date = db.Column(db.Integer,nullable= True)
    rhvalue =  db.Column(db.Integer,nullable=True)
    email=db.Column(db.Text,nullable= False)
    contact = db.Column(db.Integer,nullable=False)

@app.route('/home',methods=['GET','POST'])
def home():
    if (request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        rhvalue = request.form.get('rh')
        blood = request.form.get('blood')
        date = request.form.get('date')
        city = request.form.get('city')
        state = request.form.get('state')
        contact = request.form.get('contact')
        entry =  Donar(name=name, city=city, rhvalue=rhvalue, blood=blood,date=date,state=state,email=email,contact=contact)
        db.session.add(entry)
        db.session.commit()
        return redirect('/home')
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
    
