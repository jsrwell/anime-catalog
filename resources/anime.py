import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import anime as animes


blueprint = Blueprint('animes', __name__, description='Operations on Animes')


@blueprint.route('/anime/<anime_id>')
class Anime(MethodView):
    def get(self, anime_id):
        """GET request for an Anime."""

        try:
            return animes[anime_id]

        except KeyError:
            abort(404, message='Anime not found.')

    def put(self, anime_id):
        """PUT request for an Anime."""

        anime_data = request.json

        if "name" not in anime_data or "description" not in anime_data:
            abort(400, "Ensure 'name' and 'description' is in request.")

        try:
            anime = animes[anime_id]
            anime |= anime_data
            return anime

        except KeyError:
            abort(404, 'Anime nor found.')

    def delete(self, anime_id):
        """DELETE request for an Anime."""

        try:
            del animes[anime_id]
            return {'message': 'Anime deleted.'}

        except KeyError:
            abort(404, message='Anime not found.')


@blueprint.route('/anime')
class AnimeList(MethodView):
    def get(self):
        """GET request for the list of Animes."""

        try:
            return {"animes": list(animes.values())}

        except KeyError:
            abort(404, message='Anime not found.')

    def post(self):
        """POST request to create an Anime."""

        try:
            anime_data = request.json

            if 'name' not in anime_data:
                abort(400, message='Make sure the "name" is on request.')

            for anime in animes.values():
                if anime['name'] == anime_data['name']:
                    abort(400, message='Anime areadly exist.')

            anime_id = uuid.uuid4().hex
            anime = {'id': anime_id, **anime_data}
            animes[anime_id] = anime

            return anime

        except KeyError:
            abort(404, message='Anime not found.')
