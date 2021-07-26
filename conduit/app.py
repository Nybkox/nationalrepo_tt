import os
import logging

from loguru import logger
from flask import Flask
from dotenv import load_dotenv

from conduit.extensions import db, api
from conduit.config import DevelopmentConfig, ProductionConfig


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Retrieve context where the logging call occurred, this happens to be in the 6th frame upward
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


def create_app(config=None):
    load_dotenv()

    if config is None:
        if os.environ.get("FLASK_ENV").upper() == "DEVELOPMENT":
            config = DevelopmentConfig
        else:
            config = ProductionConfig

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    logger.start(app.config['LOG_FILE'],
                 level=app.config['LOG_LEVEL'],
                 backtrace=app.config['LOG_BACKTRACE'],
                 rotation='10 MB')
    app.logger.addHandler(InterceptHandler())

    # register all extension
    register_extensions(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    # register models
    from conduit.models.project import Project
    from conduit.models.organization import Organization
    from conduit.models.author import Author
    from conduit.models.article import Article
    from conduit.models.secondary import articles_authors, articles_fundings

    api.init_app(app)
    # register namespaces
    from conduit.api.projects import ns as projects_ns
    from conduit.api.articles import ns as articles_ns
    api.add_namespace(projects_ns, "/projects")
    api.add_namespace(articles_ns, "/articles")
