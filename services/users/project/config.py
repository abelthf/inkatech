# services/users/project/config.py

import os # nuevo

class BaseConfig:
    """Configuracion base"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False # nuevo


class DevelopmentConfig(BaseConfig):
    """Configuracion de desarrollo"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # nuevo


class TestingConfig(BaseConfig):
    """Configuracion de pruebas"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL') # nuevo


class ProductionConfig(BaseConfig):
    """Configuracion de produccion"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # nuevo
