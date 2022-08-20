from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY
from flask_wtf import Form
db = SQLAlchemy()
from tokenize import String

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.String(120), nullable=False)
    seeking_description = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String, nullable=True)
    shows = db.relationship('Show', backref='venue', lazy=True)
    genres = db.Column(db.ARRAY(db.String), default=list)
    def __repr__(self):
        return f'<Venue {self.id} {self.name} {self.city}>'

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean,nullable=False,default= False)
    seeking_description = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String, nullable=True)
    shows = db.relationship('Show', backref='artist', lazy=True)
    genres = db.Column(db.ARRAY(db.String), default=list)
    def __repr__(self):
        return f'<Artist {self.id} {self.name} {self.city}>'


class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
