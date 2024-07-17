from datetime import timedelta, date

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models.user_account import UserAccount, UserAccountSchema, user_accounts_schema, user_account_schema
from models.user import User
from init import bcrypt, db

user_account_bp = Blueprint("user_account", __name__, url_prefix="/user_accounts")

# Allow all user_accounts to be monitored
@user_account_bp.route("/")
def get_all_user_accounts():

    stmt = db.select(UserAccount).order_by(UserAccount.id)
    user_accounts = db.session.scalars(stmt)

    return user_accounts_schema.dump(user_accounts)

# Allow a user to join an user account
@user_account_bp.route("/join/<int:user_account_id>", methods=["POST"])
@jwt_required()
def join_user_account(user_account_id):
    



# Allowing the user to leave a user_account
@user_account_bp.route("/<int:user_account_id>", methods=["DELETE"])
@jwt_required()
def delete_user_account(user_account_id):
    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()

    # fetch the user_account from the db with the id
    stmt = db.select(UserAccount).filter_by(id = user_account_id)
    user_account = db.session.scalar(stmt)
    
    # if user account doesnt exist
    if not user_account:
        return {"error": f"User Account with id {user_account_id} not found"}, 404

    # only allow the user to leave the user account
    if str(user_account.user_id) != str(current_user_id):
        return {"error": "You are not authorised to remove this user account"}, 403

    # If all checks are passed
    # delete/leave user_account
    db.session.delete(user_account)
    db.session.commit()

    # return success message
    return {"message": f"User Account '{user_account.id}' deleted successfully"}
   

# Allow the admin to update user roles
@user_account_bp.route("/update/<int:user_account_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_role(user_account_id):

    # get fields from body of the request
    body_data = UserAccountSchema().load(request.get_json(), partial=True)

    # fetch the UserAccount from db
    stmt = db.select(UserAccount).filter_by(id=user_account_id)
    user_account = db.session.scalar(stmt)

    # Fetch the current user from the database
    current_user_id = get_jwt_identity()
    current_user = db.session.get(User, current_user_id)

    if not current_user:
        return {"error": "User does not exist"}, 404

    # Get fields from the body of the request
    body_data = UserAccountSchema().load(request.get_json(), partial=True)

    # Fetch the user_account from the database
    stmt = db.select(UserAccount).filter_by(id=user_account_id)
    user_account = db.session.scalar(stmt)

    if not user_account:
        return {"error": "User Account does not exist"}, 404

    # Check if the current user is an admin in the same account
    admin_stmt = db.select(UserAccount).filter_by(user_id=current_user_id, account_id=user_account.account_id, is_admin=True)
    admin_user_account = db.session.scalar(admin_stmt)

    if not admin_user_account:
        return {"error": "You are not authorised to update roles for this user account"}, 403

    # Update the fields
    user_account.role = body_data["role"] or user_account.role
    user_account.is_admin = body_data["is_admin"] or user_account.is_admin

    # Commit to the database
    db.session.commit()

    # Return a response
    return user_account_schema.dump(user_account), 200
    
