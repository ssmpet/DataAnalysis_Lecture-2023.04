import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR), "pybo.db"}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
