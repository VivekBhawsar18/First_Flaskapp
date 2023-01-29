from flask import Blueprint

bp = Blueprint('createRead' , __name__)

from app.createRead import routes