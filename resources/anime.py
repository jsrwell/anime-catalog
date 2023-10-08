"""
Anime Resources
"""
import uuid

from flask.views import MethodView
from flask_smorest import (
    Blueprint,
    abort
)

from db import anime as animes
from schemas import (
    AnimeSchema,
    AnimeUpdateSchema
)


blueprint = Blueprint('animes', __name__, description='Operations on Animes')


@blueprint.route('/anime/<anime_id>')
class Anime(MethodView):
    def get(self, anime_id):
        """Return the data of an Anime."""

        try:
            return animes[anime_id]

        except KeyError:
            abort(404, message='Anime not found.')

    @blueprint.arguments(AnimeUpdateSchema)
    def put(self, anime_data, anime_id):
        """Update the data of an Anime."""

        try:
            anime = animes[anime_id]
            anime |= anime_data
            return anime

        except KeyError:
            abort(404, 'Anime nor found.')

    def delete(self, anime_id):
        """Delete an Anime."""

        try:
            del animes[anime_id]
            return {'message': 'Anime deleted.'}

        except KeyError:
            abort(404, message='Anime not found.')


@blueprint.route('/anime')
class AnimeList(MethodView):
    def get(self):
        """Return a list of animes."""

        return {"animes": list(animes.values())}

    @blueprint.arguments(AnimeSchema)
    def post(self, new_anime):
        """Create a new anime."""

        for anime in animes.values():
            if anime['name'] == new_anime['name']:
                abort(400, message='Anime areadly exist.')

        anime_id = uuid.uuid4().hex
        anime = {'id': anime_id, **new_anime}
        animes[anime_id] = anime

        return anime
