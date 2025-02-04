import os
from flask import Flask

from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt

# Create the flask within a def
def create_app():
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

    # User
    from controllers.user_controller import user_bp
    app.register_blueprint(user_bp)

    # Account
    from controllers.account_controller import account_bp
    app.register_blueprint(account_bp)

    # UserAccount
    from controllers.user_account_controller import user_account_bp
    app.register_blueprint(user_account_bp)

    # Transaction
    from controllers.transaction_controller import transaction_bp
    app.register_blueprint(transaction_bp)

    # Category
    from controllers.category_controller import category_bp
    app.register_blueprint(category_bp)

    return app