"""
Blacklist Model
"""
from app.models.db import db


class Blacklist(db.Model):
    """Model to Control Expired Tokens."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String, nullable=False)

    def __init__(self, token):
        self.token = token
