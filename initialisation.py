from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyDB.db'
    
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    db.init_app(app)
    
    login_manageer = LoginManager()
    login_manageer.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .MyDB import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app
    
    