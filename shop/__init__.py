from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  secure_filename, FileStorage
# from flask_uploads import UploadSet
# from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
# import os




# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///t1.db"
app.config['SECRET_KEY']='jwugytdgvdt455569df'
# app.config['UPLOAD_PHOTOS_DEST']= os.path.join(basedir, 'static/images')
# photos= UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app)

#initialize the app with the extension
# db.init_app(app) 
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.app_context().push()

from shop.admin import routes
from shop.products import routes