import functools

from flask_jwt_extended import get_jwt_identity

from models.user_account import UserAccount
from init import db

def authorise_user(resource_model, resource_param, attribute_name=None, role_required=None):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # Get the current user ID from the JWT token
            current_user_id = get_jwt_identity()
            
            # Get the resource ID from the route parameters
            resource_id = kwargs.get(resource_param)
            
            # Fetch the resource (Category, Transaction, etc.)
            stmt = db.select(resource_model).filter_by(id=resource_id)
            resource = db.session.scalar(stmt)

            if not resource:
                return {"error": f"{resource_model.__name__} {resource_id} not found"}, 404

            # Dynamically determine the id for the resource
            id = getattr(resource, attribute_name, None)
            if id is None:
                return {"error": "Unable to determine account ID from resource"}, 400
            
            # Fetch user account
            user_account = db.session.query(UserAccount).filter_by(
                user_id=current_user_id, account_id=id).first()

            if not user_account:
                return {"error": "You are not authorised to perform this action for this account"}, 401

            # Check if the user's role is authorized
            if role_required and user_account.role not in role_required:
                return {"error": f"Only {', '.join(role_required)} are authorised to perform this action"}, 401

            return fn(*args, **kwargs)
        return wrapper
    return decorator