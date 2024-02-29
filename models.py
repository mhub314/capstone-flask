from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets


#set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'
    


class Folk(db.Model):
    id = db.Column(db.String, primary_key = True)
    working_title = db.Column(db.String(150))
    genre = db.Column(db.String(50))
    writer_name = db.Column(db.String(100))
    length = db.Column(db.String(15))
    rating = db.Column(db.String(50))
    latest_user_update = db.Column(db.String(50))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, working_title, genre, writer_name, length, rating, latest_user_update, user_token, id = ''):
        self.id = self.set_id()
        self.working_title = working_title
        self.genre = genre
        self.writer_name = writer_name
        self.length = length
        self.rating = rating
        self.latest_user_update = latest_user_update
        self.user_token = user_token


    def __repr__(self):
        return f'The details of your song have been logged: {self.working_title}'

    def set_id(self):
        return (secrets.token_urlsafe())

class FolkSchema(ma.Schema):
    class Meta:
        fields = ['id', 'working_title','genre','writer_name', 'length', 'rating', 'latest_user_update']

folk_schema = FolkSchema()
folks_schema = FolkSchema(many=True)

# -----------------------------------------------------------------------------------

class Rock(db.Model):
    id = db.Column(db.String, primary_key = True)
    working_title = db.Column(db.String(150))
    genre = db.Column(db.String(50))
    writer_name = db.Column(db.String(100))
    length = db.Column(db.String(15))
    rating = db.Column(db.String(50))
    latest_user_update = db.Column(db.String(50))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, working_title, genre, writer_name, length, rating, latest_user_update, user_token, id = ''):
        self.id = self.set_id()
        self.working_title = working_title
        self.genre = genre
        self.writer_name = writer_name
        self.length = length
        self.rating = rating
        self.latest_user_update = latest_user_update
        self.user_token = user_token


    def __repr__(self):
        return f'The details of your song have been logged: {self.working_title}'

    def set_id(self):
        return (secrets.token_urlsafe())

class RockSchema(ma.Schema):
    class Meta:
        fields = ['id', 'working_title','genre','writer_name', 'length', 'rating', 'latest_user_update']

rock_schema = RockSchema()
rocks_schema = RockSchema(many=True)

# -----------------------------------------------------------------------------------

class Rhythm(db.Model):
    id = db.Column(db.String, primary_key = True)
    working_title = db.Column(db.String(150))
    genre = db.Column(db.String(50))
    writer_name = db.Column(db.String(100))
    length = db.Column(db.String(15))
    rating = db.Column(db.String(50))
    latest_user_update = db.Column(db.String(50))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, working_title, genre, writer_name, length, rating, latest_user_update, user_token, id = ''):
        self.id = self.set_id()
        self.working_title = working_title
        self.genre = genre
        self.writer_name = writer_name
        self.length = length
        self.rating = rating
        self.latest_user_update = latest_user_update
        self.user_token = user_token


    def __repr__(self):
        return f'The details of your song have been logged: {self.working_title}'

    def set_id(self):
        return (secrets.token_urlsafe())

class RhythmSchema(ma.Schema):
    class Meta:
        fields = ['id', 'working_title','genre','writer_name', 'length', 'rating', 'latest_user_update']

rhythm_schema = RhythmSchema()
rhythms_schema = RhythmSchema(many=True)