from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

def create_app():
    app = Flask(__name__)
    from app.routes import main
    app.register_blueprint(main)

    return app
