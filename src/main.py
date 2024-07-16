
import os
from flask import Flask

from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt # import from init.py

def create_app(): # create the flask within a def
    app = Flask(__name__)

    app.json.sort_keys = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400
    
    @app.errorhandler(400)
    def bad_request(err):
        return {"error": err.messages}, 400
    
    # initilise controllers
    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.user_controller import user_bp
    app.register_blueprint(user_bp)

    from controllers.account_controller import account_bp
    app.register_blueprint(account_bp)

    from controllers.group_controller import group_bp
    app.register_blueprint(group_bp)

    return app