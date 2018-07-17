from flask import Flask
from apps.teachers.views import teacher
from apps.students.views import student
from apps.classes.views import classes
from apps.ext import init_app

app = Flask(__name__)


def get_app():
    app.debug = True
    register_blue()
    init_app(app)
    return app


def register_blue():
    app.register_blueprint(student, url_prefix='/student')
    app.register_blueprint(teacher, url_prefix='/teacher')
    app.register_blueprint(classes, url_prefix='/classes')