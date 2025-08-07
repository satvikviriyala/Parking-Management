# Configuration settings for the Flask application
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/database.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
