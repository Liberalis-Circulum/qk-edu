from apps.ext import db


class Students(db.Model):
    STATUS = {
        '休学': 0,
        '在读': 1,
        '请假': 2,
        '毕业': 3,
        '辍学': 4,
    }
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True, nullable=False)
    pwd = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(32), index=True, nullable=False)
    # 头像
    head_img = db.Column(db.String(64))
    # 入学年
    period = db.Column(db.Integer, nullable=False)
    # 性别
    sex = db.Column(db.Boolean, nullable=False)
    # 年龄
    old = db.Column(db.Integer)
    # 班级
    cls = db.Column(db.Integer, db.ForeignKey('classes.cid'))
    is_status = db.Column(db.Integer)