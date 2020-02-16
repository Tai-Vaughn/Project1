from flask import Flask
from flask_mail import Mail

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'mudamudamuda'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 4652525)

app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = '' 
mail = Mail(app)
from app import views