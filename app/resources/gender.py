"""
Gender Resources
"""
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from app.models.db import db
from app.models.gender import Gender
from app.schemas.gender import GenderSchema, GenderUpdateSchema

blueprint = Blueprint('Genders', __name__, description='Genders of the Animes')


@blueprint.route('/gender/<int:gender_id>')
class GenderView(MethodView):
    """Gender View."""

    @blueprint.response(200, GenderSchema)
    def get(self, gender_id):
        """Return the data of a Gender."""

        gender = Gender.query.get(gender_id)

        if not gender:
            abort(404, message='Gender not found.')

        return gender

    @jwt_required(fresh=True)
    @blueprint.response(200, GenderSchema)
    @blueprint.arguments(GenderUpdateSchema)
    def put(self, gender_data, gender_id):
        """Update the data of a Gender."""

        gender = Gender.query.get(gender_id)

        if not gender:
            abort(404, message='Gender not found.')

        for key, value in gender_data.items():
            setattr(gender, key, value)

        try:
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            abort(400, message=f'Error updating gender: {str(e)}')

        return gender

    @jwt_required(fresh=True)
    def delete(self, gender_id):
        """Delete a Gender."""

        gender = Gender.query.get(gender_id)

        if not gender:
            abort(404, message='Gender not found.')

        try:
            db.session.delete(gender)
            db.session.commit()

            return {'message': 'Gender deleted.'}

        except Exception as e:
            db.session.rollback()
            abort(400, message=f'Error deleting gender: {str(e)}')


@blueprint.route('/gender')
class GenderListView(MethodView):
    """Gender List View."""

    @blueprint.response(200, GenderSchema(many=True))
    def get(self):
        """Return a list of genders."""

        genders = Gender.query.all()

        return genders

    @jwt_required(fresh=True)
    @blueprint.response(201, GenderSchema)
    @blueprint.arguments(GenderSchema)
    def post(self, new_gender):
        """Create a new gender."""

        try:
            gender = Gender(**new_gender)
            db.session.add(gender)
            db.session.commit()

            return gender, 201

        except Exception as e:
            db.session.rollback()
            abort(400, message=f'Error creating gender: {str(e)}')
