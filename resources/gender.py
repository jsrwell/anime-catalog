import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import gender as genders


blueprint = Blueprint('genders', __name__, description='Operations on Genders')


@blueprint.route('/gender/<gender_id>')
class Gender(MethodView):
    def get(self, gender_id):
        """GET request for an Gender."""

        try:
            return genders[gender_id]

        except KeyError:
            abort(404, message='Gender not found.')

    def put(self, gender_id):
        """PUT request for an Gender."""

        gender_data = request.json

        if "name" not in gender_data or "description" not in gender_data:
            abort(400, "Ensure 'name' and 'description' is in request.")

        try:
            gender = genders[gender_id]
            gender |= gender_data
            return gender

        except KeyError:
            abort(404, 'Gender nor found.')

    def delete(self, gender_id):
        """DELETE request for an Gender."""

        try:
            del genders[gender_id]
            return {'message': 'Gender deleted.'}

        except KeyError:
            abort(404, message='Gender not found.')


@blueprint.route('/gender')
class GenderList(MethodView):
    def get(self):
        """GET request for the list of Genders."""

        try:
            return {"genders": list(genders.values())}

        except KeyError:
            abort(404, message='Gender not found.')

    def post(self):
        """POST request to create an Gender."""

        try:
            gender_data = request.json

            if 'name' not in gender_data:
                abort(400, message='Make sure the "name" is on request.')

            for gender in genders.values():
                if gender['name'] == gender_data['name']:
                    abort(400, message='Gender areadly exist.')

            gender_id = uuid.uuid4().hex
            gender = {'id': gender_id, **gender_data}
            genders[gender_id] = gender

            return gender

        except KeyError:
            abort(404, message='Gender not found.')
