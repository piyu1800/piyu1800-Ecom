from shop import db
from shop import app



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password= db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')


    def __repr__(self) :
        return '<User %r>' % self.username

@app.before_first_request
def create_table():
    db.create_all()


      