from typing import Any

from flask import Flask
from flask_cors import CORS


def init_app(config_file_path: str = "settings.py", **config: Any) -> Flask:
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile(config_file_path)
    app.config.update(**config)

    # Initialize Plugins
    CORS(app)

    with app.app_context():
        from . import api

        app.register_blueprint(api.api_bp)
        return app
