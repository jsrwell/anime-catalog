from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Gender(db.Model):
    """Model for the Gender of an Anime."""

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name
