from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    # __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(5))
    location = db.Column(db.String(100))
    biography = db.Column(db.String(200))
    photo = db.Column(db.String(80))
    def __init__(self,fname,lname ,email ,gender , location, biography,photo):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.gender = gender
        self.location = location
        self.biography = biography
        self.photo = photo
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)