# app/__init__.py

from flask import Flask
from .routes import register_routes
import yaml

def create_app():
    app = Flask(__name__)

    # Load route configuration from YAML file
    with open('app/config/routes.yml', 'r') as file:
        routes_config = yaml.safe_load(file)

    register_routes(app, routes_config)

    return app
