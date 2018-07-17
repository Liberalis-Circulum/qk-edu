from apps.ext import db


class Classes(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True, unique=True, nullable=False)
    chinese = db.Column(db.Integer, db.ForeignKey('teachers.tid'))
    math = db.Column(db.Integer, db.ForeignKey('teachers.tid'))
    english = db.Column(db.Integer, db.ForeignKey('teachers.tid'))
    sport = db.Column(db.Integer, db.ForeignKey('teachers.tid'))
    is_status = db.Column(db.Integer, nullable=False)