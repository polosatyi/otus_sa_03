# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from .metrics import register_metrics


db = SQLAlchemy()
alembic = Alembic()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    alembic.init_app(app)
    register_metrics(app)

    with app.app_context():
        from . import models
        from . import routes
        return app
