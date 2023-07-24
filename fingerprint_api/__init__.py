from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Set up the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fingerprint.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.init_app(app)

    # Enable CORS for all routes
    CORS(app)
    
    with app.app_context():
        # Import and register blueprints here if you have multiple blueprints
        from fingerprint_api.views import fingerprint_blueprint
        app.register_blueprint(fingerprint_blueprint)

        # Create the database tables
        db.create_all()


    return app