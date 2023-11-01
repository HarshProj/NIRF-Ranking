from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class User (db.Model):
    id=db.Column(db.Integer,primary_key)
    id=db.Column(db.Integer,primary_key)

@app.route('/')
def hell():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,port=3000)