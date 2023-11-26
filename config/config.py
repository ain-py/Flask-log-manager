# config/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:toor@localhost/site'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
