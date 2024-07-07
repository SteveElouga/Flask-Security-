from .views import app
from .models import db
from .models import init_db
from .auth import auth_bp, jwt
from flask_migrate import Migrate
from .users import users_bp

migrate = Migrate(app, db)
jwt.init_app(app)
db.init_app(app)
app.register_blueprint(auth_bp, url_prefix = '/auth')
app.register_blueprint(users_bp, url_prefix="/users")