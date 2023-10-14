"""
Models - User
"""
from app.models.db import db


class UserModel(db.Model):
    """Model for the Users of the Catalog."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
