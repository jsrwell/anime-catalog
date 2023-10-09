"""
Gender Resources
"""
import uuid

from flask.views import MethodView
from flask_smorest import (
    Blueprint,
    abort
)

from db import gender as genders
from schemas import (
    GenderSchema,
    GenderUpdateSchema
)


blueprint = Blueprint('Genders', __name__, description='Genders of the Animes')


@blueprint.route('/gender/<gender_id>')
class Gender(MethodView):
    """Gender of the Animes."""

    @blueprint.response(200, GenderSchema)
    def get(self, gender_id):
        """Return the data of an Gender."""

        try:
            return genders[gender_id]

        except KeyError:
            abort(404, message='Gender not found.')

    @blueprint.response(200, GenderSchema)
    @blueprint.arguments(GenderUpdateSchema)
    def put(self, gender_data, gender_id):
        """Update the data of an Gender."""

        try:
            gender = genders[gender_id]
            gender |= gender_data
            return gender

        except KeyError:
            abort(404, 'Gender nor found.')

    def delete(self, gender_id):
        """Delete an Gender."""

        try:
            del genders[gender_id]
            return {'message': 'Gender deleted.'}

        except KeyError:
            abort(404, message='Gender not found.')


@blueprint.route('/gender')
class GenderList(MethodView):
    """Genders of the Animes."""

    @blueprint.response(200, GenderSchema(many=True))
    def get(self):
        """Return a list of genders."""

        return list(genders.values())

    @blueprint.response(201, GenderSchema)
    @blueprint.arguments(GenderSchema)
    def post(self, new_gender):
        """Create a new gender."""

        for gender in genders.values():
            if gender['name'] == new_gender['name']:
                abort(400, message='Gender areadly exist.')

        gender_id = uuid.uuid4().hex
        gender = {'id': gender_id, **new_gender}
        genders[gender_id] = gender

        return gender
