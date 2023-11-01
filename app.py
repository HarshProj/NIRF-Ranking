from flask import Flask, render_template, request, redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from bcrypt import hashpw, checkpw, gensalt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key="HARSHHERE"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"
        
    def __init__(self,id, name, email, password):
        self.id=id
        self.name = name
        self.email = email
        self.password = hashpw(password.encode('utf-8'), gensalt())

    def checkpass(self, password):
        return checkpw(password.encode('utf-8'), self.password)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.checkpass(password):
            session['name']=user.name
            session['email']=user.email
            session['password']=user.name
            return redirect('/')
        else:
            return render_template('login.html', error="Invalid User")
    return render_template('Login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = User(id=1,name=name, email=email, password=password)
        # print(user.email)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)
