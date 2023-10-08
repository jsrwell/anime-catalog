"""
App - Anime Catalog
"""
from flask import Flask
from flask_smorest import Api
from resources.anime import blueprint as AnimeBlueprint
from resources.gender import blueprint as GenderBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Animes Catalog REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # noqa E501

api = Api(app)
api.register_blueprint(AnimeBlueprint)
api.register_blueprint(GenderBlueprint)
