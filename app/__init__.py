from flask_migrate import Migrate
from app.resources.gender import blueprint as GenderBlueprint
from app.resources.anime import blueprint as AnimeBlueprint
from flask import Flask
from flask_smorest import Api
from app.models.db import db

api = Api()

app = Flask(__name__)
app.config.from_pyfile('config.py')
migrate = Migrate(app, db)
db.init_app(app)
api.init_app(app)

api.register_blueprint(AnimeBlueprint)
api.register_blueprint(GenderBlueprint)
