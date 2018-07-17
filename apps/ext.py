# 用于第三方插件的配置
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_mail import Mail
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_cors import CORS
from flask_login import LoginManager


def init_app(app):
    init_db_config(app)
    init_cache_config(app)
    init_upload_config(app)
    init_mail_config(app)
    init_cors_init(app)
    init_login_config(app)


# 配置数据库以及迁移
db = SQLAlchemy()
migrate = Migrate()


def init_db_config(app):
    app.config['SECRET_KEY'] = 'edu'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/edu?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)


# 配置缓存
cache = Cache()


def init_cache_config(app):
    cache.init_app(app, config={
        'CACHE_DEFAULT_TIMEOUT': 60*10,
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': '127.0.0.1',
        'CACHE_REDIS_PORT': '6379',
        'CACHE_REDIS_DB':'1',
        'CACHE_KEY_PREFIX':'view_'
    })


# 配置邮箱
mail = Mail()


def init_mail_config(app):
    mail.init_app(app)
    app.config["MAIL_SERVER"] = "smtp.163.com"
    app.config["MAIL_PORT"] = 25
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = "18008640170@163.com"
    app.config["MAIL_PASSWORD"] = "qukang061795"


# 文件上传
images = UploadSet(name='images', extensions=IMAGES)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR, 'static')


def init_upload_config(app):
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_ROOT_PATH
    app.config['UPLOADS_DEFAULT_URL'] = 'http://127.0.0.1:2333/apps/static'
    configure_uploads(app=app, upload_sets=images)


# 设置跨域请求
def init_cors_init(app):
    CORS(app,  supports_credentials=True)


# 设置保持登录
login_manager = LoginManager()


def init_login_config(app):
    login_manager.login_view = 'students.log'
    login_manager.login_message = '请先登录'
    login_manager.init_app(app)