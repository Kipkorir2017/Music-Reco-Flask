from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    review = db.relationship('Review', backref='user', lazy="dynamic")
    song = db.relationship('Song', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'



class Review(db.Model):

    """
    User review model for each song 
    """
    __tablename__ = 'reviews'

    #table columns
    id = db.Column(db.Integer, primary_key=True)
    opinion = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))
    # song = db.relationship('Song', backref='reviews', lazy="dynamic")
    

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(self, id):
        review = Review.query.order_by(
            Review.time_posted.desc()).filter_by(reviews_id=id).all()
        return review

class Song(db.Model):
    __tablename__="songs"

    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255))
    category = db.Column(db.String(255))
    artist = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    review_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    review = db.relationship('Review',backref= 'song', lazy="dynamic")

    def save_song(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_songs(cls, category):
        songs = Song.query.filter_by(category=category).all()
        return songs
    @classmethod
    def getSongId(cls, id):
        song = Song.query.filter_by(id=id).first()
        return song
    @classmethod
    def clear_songs(cls):
        Song.all_songs.clear()
