from flask import Blueprint
from apps.classes.models import Classes
from apps.students.models import Students
from apps.teachers.models import Teachers

student = Blueprint('student', __name__)
