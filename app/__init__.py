from flask import Flask

from .api.routes import api_bp
from .config import get_config

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    app.register_blueprint(api_bp)

    @app.get("/")
    def home():
        return {"name": "food-list", "status": "ok"}
    
    return app