from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    votes = db.relationship('Vote', backref='voter', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(120), index=True, unique=True)
    choice_1 = db.Column(db.String(64), index=True)
    choice_2 = db.Column(db.String(64), index=True)
    votes = db.relationship('Vote', backref='poll', lazy='dynamic')

    def __repr__(self):
        return '<Poll {}>'.format(self.question)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote_choice = db.Column(db.Boolean(), index=True)
    poll_id = db.Column(db.String(120), db.ForeignKey('poll.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Vote {} {} {}>'.format(self.user_id, self.poll_id, self.vote_choice)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

    