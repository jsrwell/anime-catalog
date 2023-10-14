from flask_migrate import Migrate
from app.resources.gender import blueprint as GenderBlueprint
from app.resources.anime import blueprint as AnimeBlueprint
from app.resources.user import blueprint as UserBlueprint
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from app.models.db import db
from app.models.blacklist import Blacklist

api = Api()
app = Flask(__name__)

app.config.from_pyfile('config.py')

migrate = Migrate(app, db)
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_the_token_is_in_blacklist(jwt_header, jwt_payload):
    blacklist_all = Blacklist.query.all()
    blacklist = [blacklist.token for blacklist in blacklist_all]
    return jwt_header['jti'] in blacklist


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        "description": "Token has expired!",
        "error": "token_expired"
    }, 401)


@jwt.invalid_token_loader
def invalid_token_callback():
    return jsonify({
        "description": "Signature verification failed!",
        "error": "invalid_token"
    }, 401)


@jwt.unauthorized_loader
def unauthorized_loader_callback(error):
    return jsonify({
        "description": "Access token not found!",
        "error": "unauthorized_loader"
    }, 401)


@jwt.needs_fresh_token_loader
def fresh_token_loader_callback():
    return jsonify({
        "description": "Token is not fresh. Fresh token needed!",
        "error": "needs_fresh_token"
    }, 401)


db.init_app(app)
api.init_app(app)

api.register_blueprint(AnimeBlueprint)
api.register_blueprint(GenderBlueprint)
api.register_blueprint(UserBlueprint)
