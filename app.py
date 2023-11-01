from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class User (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),primary_key=True)
    email=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(100),nullable=False)

@app.route('/')
def hell():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__=="__main__":
    app.run(debug=True,port=3000)