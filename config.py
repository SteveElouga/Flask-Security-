import os


FLASK_SECRET_APP = 'o[9QS!ceFmB-\rc-\rb$G2\x0b~o['
FLASK_DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db' )
SQLALCHEMY_ECHO = True
JWT_SECRET_KEY = 'aacea25fa765eedf10488fef'