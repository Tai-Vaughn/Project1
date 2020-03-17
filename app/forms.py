from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ContactForm(FlaskForm):
    fname = StringField('First name', validators=[InputRequired()])
    lname = StringField('Last name', validators=[InputRequired()])
    email= StringField('Email',validators=[Email(),InputRequired()])
    gender = SelectField ('Gender', choices=[('M','Male'),('F' , 'Female')])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])