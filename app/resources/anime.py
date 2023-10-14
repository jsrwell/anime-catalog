"""
Anime Resources
"""
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from app.models.db import db
from app.models.anime import Anime
from app.schemas.anime import AnimeSchema, AnimeUpdateSchema

blueprint = Blueprint('Animes', __name__, description='Animes on the Catalog')


@blueprint.route('/anime/<int:anime_id>')
class AnimeView(MethodView):
    """Anime View."""

    @blueprint.response(200, AnimeSchema)
    def get(self, anime_id):
        """Return the data of an Anime."""

        anime = Anime.query.get(anime_id)

        if not anime:
            abort(404, message='Anime not found.')

        return anime

    @jwt_required(fresh=True)
    @blueprint.response(200, AnimeSchema)
    @blueprint.arguments(AnimeUpdateSchema)
    def put(self, anime_data, anime_id):
        """Update the data of an Anime."""

        anime = Anime.query.get(anime_id)

        if not anime:
            abort(404, message='Anime not found.')

        for key, value in anime_data.items():
            setattr(anime, key, value)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(400, message=f'Error updating anime: {str(e)}')

        return anime

    @jwt_required(fresh=True)
    def delete(self, anime_id):
        """Delete an Anime."""

        anime = Anime.query.get(anime_id)
        if not anime:
            abort(404, message='Anime not found.')

        try:
            db.session.delete(anime)
            db.session.commit()

            return {'message': 'Anime deleted.'}

        except Exception as e:
            db.session.rollback()
            abort(400, message=f'Error deleting anime: {str(e)}')


@blueprint.route('/anime')
class AnimeListView(MethodView):
    """Anime List View."""

    @blueprint.response(200, AnimeSchema(many=True))
    def get(self):
        """Return a list of animes."""

        animes = Anime.query.all()

        return animes

    @jwt_required(fresh=True)
    @blueprint.response(201, AnimeSchema)
    @blueprint.arguments(AnimeSchema)
    def post(self, new_anime):
        """Create a new anime."""

        try:
            anime = Anime(**new_anime)
            db.session.add(anime)
            db.session.commit()

            return anime, 201

        except ValidationError as ve:
            abort(400, messages=ve.messages)

        except Exception as e:
            db.session.rollback()
            abort(400, message=f'Error creating anime: {str(e)}')
