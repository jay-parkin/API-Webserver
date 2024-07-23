from datetime import timedelta, date

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models.user import User, user_schema, UserSchema
from init import bcrypt, db

# handles errors
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

user_bp = Blueprint("user", __name__, url_prefix="/users")

# Allow users to register to the app
@user_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # Get the date from the body
        body_data = UserSchema().load(request.get_json())

        # Create an instance of the User model
        user = User(
            name = body_data.get("name"),
            email = body_data.get("email"),
            created_at = date.today()
        )

        # Extract pass from the body
        password = body_data.get("password_hash")

        # Hash the password
        if password:
            user.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        # Add and commit to the db
        db.session.add(user)
        db.session.commit()

        # Respond back
        return user_schema.dump(user), 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409

        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409
        
# Allow the user to login their account
@user_bp.route("/login", methods=["POST"])
def login_user():
    # Get data from the body of the request
    body_data = request.get_json()
    
    # Find the user with the email
    stmt = db.select(User).filter_by(email = body_data.get("email"))
    user = db.session.scalar(stmt)
    
    # If user exists? and password is correct?
    if user and bcrypt.check_password_hash(user.password_hash, body_data.get("password_hash")):
        # Create jwt
        token = create_access_token(identity = str(user.id), expires_delta = timedelta(days = 1))

        # Respond back
        return {"email": user.email, "token": token}

    else:
        # Respond back with error message
        return {"error": "Invalid email or password"}, 401 # Unauthenicated
    
# Allow the user to only update themselves
@user_bp.route("/update", methods=["PUT", "PATCH"])
@jwt_required()
def update_user():
    # Get fields from body of the request
    body_data = UserSchema().load(request.get_json(), partial=True)
    password = body_data.get("password_hash")

    # Fetch the user from db
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)

    # If user exist
    if user:
        # Update the fields
        user.name = body_data.get("name", user.name)
        
        if password:
            user.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        # Commit to the db
        db.session.commit()

        # Return a response
        return user_schema.dump(user)

    else:
        # Return an error
        return {"error": "User does not exist"}, 404

# Allows the user to only delete themselves
@user_bp.route("/delete", methods=["DELETE"])
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()

    # Find the user
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)

    # If user exists
    if user:
        # Delete the user
        db.session.delete(user)

        # Commit to the DB
        db.session.commit()

        # Return a message
        return {"message": f"User with id {user.id} deleted"}

    else:
        # Return error saying user does not exist
        return {"error": "User does not exist"}, 404