from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Anime(db.Model):
    """Model for Anime."""

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    gender_id = db.Column(db.String, db.ForeignKey(
        'gender.id'), nullable=False)

    gender = db.relationship('Gender', backref='animes')

    def __init__(self, name, description, gender_id):
        self.name = name
        self.description = description
        self.gender_id = gender_id
