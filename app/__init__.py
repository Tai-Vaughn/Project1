from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)

app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ddbdugprosrwsp:424e2260898e422727e1b3b3c61281f057b01bbf9e5f1fd61a1adf4fa3d236d0@ec2-50-17-178-87.compute-1.amazonaws.com:5432/dau4fpsqfstnqg"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = '/app/static/uploads'

db = SQLAlchemy(app)
from app import views