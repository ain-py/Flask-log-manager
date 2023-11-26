
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:toor@db:5432/site'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my-super-key'