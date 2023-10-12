"""
Anime Model
"""
from app.models.db import db


class Anime(db.Model):
    """Model for Anime."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey(
        'gender.id'), nullable=False)

    gender = db.relationship('Gender', backref='animes')

    def __init__(self, name, description, gender_id):
        self.name = name
        self.description = description
        self.gender_id = gender_id
