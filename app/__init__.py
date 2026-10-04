from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')


db = SQLAlchemy(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)

from app import routes
from app.models import usuario 