import os

class BaseConfig: 
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False

def get_config(name: str):
    mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    if name:
        return mapping.get(name, DevelopmentConfig)
    env_name = os.getenv("FLASK_ENV", "development")
    return mapping.get(name, DevelopmentConfig)