"""
Users Resources
"""
from passlib.hash import pbkdf2_sha256
from flask.views import MethodView
from flask_smorest import (
    Blueprint,
    abort
)
from flask_jwt_extended import (
    create_access_token,
    get_jti,
    jwt_required,
    create_refresh_token,
    get_jwt_identity,
)

from app.models.db import db
from app.models.user import UserModel
from app.schemas.user import UserSchema
from app.models.blacklist import Blacklist

blueprint = Blueprint('Users', __name__, description='Users of the Catalog')


@blueprint.route('/register')
class UserRegister(MethodView):
    """View to User register."""

    @blueprint.arguments(UserSchema)
    def post(self, user_data):
        """Register an User."""

        if UserModel.query.get(user_data["username"]):
            abort(409, message="This username areadly exists.")

        user = UserModel(
            username=user_data['username'],
            password=pbkdf2_sha256.hash(user_data['password'])
        )
        db.session.add(user)
        db.session.commit()

        return {'message': 'User created sucessfully'}, 201


@jwt_required(fresh=True)
@blueprint.route('/user/<int:user_id>')
class User(MethodView):
    """View to User."""

    @blueprint.response(200, UserSchema)
    def get(self, user_id):
        """Return the data of an User."""

        anime = User.query.get(user_id)

        if not anime:
            abort(404, message='User not found.')

        return anime


@blueprint.route('/login')
class UserLogin(MethodView):
    """View to User Login."""

    @blueprint.arguments(UserSchema)
    def post(self, user_data):
        """Make the user Login."""

        user = UserModel.query.filter_by(
            username=user_data['username']).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        abort(401, message='Invalid Credentials.')


@jwt_required(fresh=True)
@blueprint.route('/logout')
class UserLogout(MethodView):
    """View to User Logout."""

    @blueprint.arguments(UserSchema)
    def delete(self):
        """Make the user logout."""

        jti = get_jti()["jti"]
        blacklist = Blacklist(token=jti)
        db.session.add(blacklist)
        db.session.commit()

        return {"message": "Successfully logged out"}, 200


@blueprint.route('/refresh')
class TokenRefresh(MethodView):
    """View to Handle the Fresh Token."""

    def post(self):
        """Get a new access token."""

        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        jti = get_jti()["jti"]
        blacklist = Blacklist(token=jti)
        db.session.add(blacklist)
        db.session.commit()

        return {'access_token': new_token}, 200
