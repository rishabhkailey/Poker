from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Student(db.Model):
	id = db.Column(db.Integer,primary_keys = True)
	name = db.Column(db.String)
	cgpa = db.Column(db.Float)
	branch = db.Column(db.String)

if __name__ = '__main__':
	print(app.config)
	app.config['DEBUG'] = True
	app.config['SQLALCHEMY_DATABASE_URL'] = "postgresql://postgres:password@localhost:5432/student"
	db.create_all()
	app.run(port = 8080)0