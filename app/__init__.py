from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager
from pathlib import Path
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
Path(app.instance_path).mkdir(parents=True, exist_ok=True)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para acessar esta página.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    from app.models.usuario import Usuario
    return Usuario.query.get(int(user_id))


from app import routes
from app.models import usuario, categoria, objeto, devolucao