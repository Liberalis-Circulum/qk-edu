from apps.ext import db


class Teachers(db.Model):
    STATUS = {
        '离职': 0,
        '在职': 1,
        '在假': 2,
    }
    SUBJECT = {
        '语文': 1,
        '数学': 2,
        '体育': 3,
        '英语': 4,
    }
    tid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True, nullable=False)
    pwd = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(32), index=True, unique=True, nullable=False)
    head_img = db.Column(db.String(64))
    # 学科
    subject = db.Column(db.Integer)
    # 是否删除
    is_status = db.Column(db.Integer, nullable=False)
