"""
Gender Model
"""
from app.models.db import db


class Gender(db.Model):
    """Model for the Gender of an Anime."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name
