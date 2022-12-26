
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate
# from werkzeug.utils import import_string
# import werkzeug
# werkzeug.import_string = import_string

# import flask_cache
# from werkzeug import import_string


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///t1.db'
app.config['SECRET_KEY']='hfouewhfoiwefoquw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
# app.config['UPLOADED_PHOTOS_ALLOW'] = set(['png', 'jpg', 'jpeg'])
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)


migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

login_manager= LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.login_message_category='danger'
login_manager.login_message=u"Please Login First"
app.app_context().push()

from shop.admin import routes
from shop.products import routes
from shop.carts import carts
from shop.customers import routes