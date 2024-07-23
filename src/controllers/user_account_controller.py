from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from utils import authorise_user

from models.user_account import UserAccount, UserAccountSchema, user_account_schema
from init import db

user_account_bp = Blueprint("user_account", __name__, url_prefix="/user_accounts")

# Allowing the user to leave a user_account
@user_account_bp.route("/<int:user_account_id>", methods=["DELETE"])
@jwt_required()
def delete_user_account(user_account_id):
    # Fetch the user_account from the db with the id
    stmt = db.select(UserAccount).filter_by(id = user_account_id)
    user_account = db.session.scalar(stmt)
    
    # If user account doesnt exist
    if not user_account:
        return {"error": f"User Account with id {user_account_id} not found"}, 404
    
    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()
    # Fetch the current user
    current_user = db.session.query(UserAccount).filter_by(id=current_user_id).first()
   
    if not current_user:
         return {"error": "You are not found"}, 401
    
    # Check if the current user is an admin
    if current_user.is_admin:
        # Admins can only delete users from the same account
        if current_user.account_id != user_account.account_id:
            return {"error": "You are not authorised to remove this user account"}, 401

        # Delete user as admin
        db.session.delete(user_account)
        db.session.commit()

        # Return success message
        return {"message": f"User Account '{user_account.id}' deleted successfully"}, 200

     # Regular users can only delete their own account
    if str(user_account.user_id) != str(current_user_id):
        return {"error": "You are not authorised to remove this user account"}, 401

    # If all checks are passed
    # Delete/leave user_account
    db.session.delete(user_account)
    db.session.commit()

    # return success message
    return {"message": f"User Account '{user_account.id}' deleted successfully"}, 200
   
# Allow the admin to update user roles
@user_account_bp.route("/update/<int:user_account_id>", methods=["PUT", "PATCH"])
@jwt_required()
@authorise_user(resource_model=UserAccount, 
                resource_param="user_account_id", 
                attribute_name="account_id",
                role_required=["Admin"])
def update_role(user_account_id):
    # Get fields from body of the request
    body_data = UserAccountSchema().load(request.get_json(), partial=True)

    # Fetch the UserAccount from db
    stmt = db.select(UserAccount).filter_by(id=user_account_id)
    user_account = db.session.scalar(stmt)

    if not user_account:
        return {"error": "User Account does not exist"}, 404

    # Update the fields
    user_account.role = body_data.get("role", user_account.role)

    if user_account.role == "Admin":
        user_account.is_admin = True
    
    else:
        user_account.is_admin = False

    # Commit to the database
    db.session.commit()

    # Return a response
    return user_account_schema.dump(user_account), 200