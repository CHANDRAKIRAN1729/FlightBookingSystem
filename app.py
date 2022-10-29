from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
pymysql.install_as_MySQLdb()

#Conencting to the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/airline'
db = SQLAlchemy(app)


class users(db.Model):
    '''
    uid, uname, password
    '''
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(22), nullable=False)
    password = db.Column(db.String(20), nullable=False)


class bookings(db.Model):
    '''
    bid,uid,arrival,departure
    '''
    bid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable = False)
    arrival = db.Column(db.String(20), nullable=False)
    departure = db.Column(db.String(30), nullable=False)


#route for registration page

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if(request.method=='POST'):
        '''Add entry to the database'''
        username = request.form.get('uname')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')

        entry = users(username= username, age = age, email = email, password = password)
        db.session.add(entry)
        db.session.commit()
    return render_template('booking.html')


#route for registration page

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'):

        username = request.form.get('uname')
        password = request.form.get('password')

        entry = users.query.filter_by(username=username, password=password).first()
        if entry:
            return render_template('fail.html')
        else:
            return render_template('booking.html')
    return render_template('login.html')



# Route for booking page

@app.route("/booking", methods = ['GET', 'POST'])
def booking():
    if(request.method=='POST'):
        '''Add entry to the database'''
        bid = request.form.get('bid')
        arrival = request.form.get('arrival')
        departure = request.form.get('departure')

        entry = users(bid = bid, arrival = arrival , departure = departure)
        db.session.add(entry)
        db.session.commit()
    return render_template('successbook.html')


app.run(debug=True)
