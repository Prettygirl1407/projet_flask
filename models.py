from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyDB.db'
db = SQLAlchemy(app)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(1500))
    firstname = db.Column(db.String(1500))
    email = db.Column(db.String(500), unique=True)
    password = db.Column(db.String(300))
    
db.create_all()    

@app.route('/')
def dac():
    return "Daciana"

if __name__ == "__main__":
    app.run(debug=True)