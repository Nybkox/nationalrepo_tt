import os


dp = os.path.abspath(os.getcwd())


class DevelopmentConfig:
    # Basic configuration
    DEBUG = True
    SECRET_KEY = "secret"

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{dp}/dev_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # loguru configuration
    LOG_BACKTRACE = True
    LOG_LEVEL = 'DEBUG'
    LOG_FILE = f'{dp}/logs/dev.log'


class ProductionConfig:
    # Basic configuration
    DEBUG = False
    SECRET_KEY = "secret"

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{dp}/prod_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # loguru configuration
    LOG_BACKTRACE = True
    LOG_LEVEL = 'INFO'
    LOG_FILE = f'{dp}/logs/prod.log'

