from flask import Flask
from config import Config
from app.extensions import db

app = Flask(__name__)

# App configuration
app.config.from_object(Config)

# Initialize Flask extensions here
db.init_app(app)

# Register blueprints here

from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app.posts import bp as posts_bp
app.register_blueprint(posts_bp, url_prefix='/posts')

from app.questions import bp as questions_bp
app.register_blueprint(questions_bp, url_prefix='/questions')

from app.createRead import bp as create_bp
app.register_blueprint(create_bp , url_prefix='/createRead')