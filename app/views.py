"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from  app import app
from flask import render_template, request, redirect, url_for, flash
from flask_mail import Message
from werkzeug.utils import secure_filename
from .forms import ContactForm
from .model import UserProfile
from .db_data import getdata
from . import db

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile', methods=['GET','POST'])
def profile():
    myform = ContactForm()
    if request.method == 'POST':
            photo = myform.photo.data 

            filename = secure_filename(photo.filename)
            path = os.path.join(
                '.'+app.config['UPLOAD_FOLDER'], filename
            )
            photo.save(path)
            photo.save(path)

            user = UserProfile( 
            fname=myform.fname.data,lname=myform.lname.data,
            email= myform.email.data,gender=myform.gender.data, location=myform.location.data,
            biography= myform.biography.data, photo=path)

            db.session.add(user)
            db.session.commit()
            flash('Email was sent!!')
            return redirect(url_for('home'))
    return render_template ('profile.html', form=myform)

@app.route('/profiles')
def profiles():
    user_records = getdata()
    return render_template('profiles.html', data=user_records)
###
# The functions below should be applicable to all Flask apps.
###


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def  get_uploaded_images():
    rootdir = os.getcwd()
    links = []
    for subdir, dirs, files in os.walk(rootdir + app.config['UPLOAD_FOLDER']):
        for file in files:
            links.append(file)
        links.pop(links.index(".gitkeep"))
        return links
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
