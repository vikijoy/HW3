import secrets

class Config(object):
    SERVER_NAME = 'localhost:5000'
    SECRET_KEY = secrets.token_hex()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
