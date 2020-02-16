from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired

class ContactForm(FlaskForm):
    name= StringField('Name',validators=[DataRequired(),InputRequired()])
    email= StringField('Email',validators=[Email(),InputRequired()])
    subject= StringField('Subject',validators=[DataRequired()])
    textArea= TextAreaField('Message',validators=[DataRequired()])