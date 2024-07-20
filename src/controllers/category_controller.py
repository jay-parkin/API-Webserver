
from datetime import date, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.category import Category, categories_schema, category_schema
from models.account import Account
from models.user_account import UserAccount

from init import db

category_bp = Blueprint("categories", __name__, url_prefix="/categories")

# Allow all category to be monitored
@category_bp.route("/")
def get_all_categories():
    
    stmt = db.select(Category).order_by(Category.id)
    categories = db.session.scalars(stmt)

    return categories_schema.dump(categories)

# Allow user to fetch category by ID
@category_bp.route("/<int:category_id>", methods=["GET"])
def get_category(category_id):

    # fetch category from database
    stmt = db.select(Category).filter_by(id=category_id)
    category = db.session.scalar(stmt)

    if not category:
        return {"error": "Category not found"}, 404
    
    return category_schema.dump(category)

# Allow only admin or contributors to create a new transactions
@category_bp.route("/create/<int:account_id>", methods=["POST"])
@jwt_required()
def create_category(account_id):
    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()

    # fetch the account from database
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": "Account does not exist"}, 404

    # fetch user account
    # Check to see if the current user is apart of the user_account
    user_account = db.session.query(UserAccount).filter_by(
        user_id=current_user_id, account_id=account_id).first()

    if not user_account:
        return {"error": "You are not authorised to create a category for this account"}, 401
    
    # Check if the user's role is "Viewer"
    if user_account.role == "Viewer":
        return {"error": "Viewers not authorised to create categories"}, 401
    
    # Fetch the category from the body
    body_data = request.get_json()
    category_name = body_data.pop("category_name")

    # create a new category instance
    if not category_name:     
        return {"error": "Category name is needed"}, 400   
   
     # create the category if it doesn't exist
    category = Category(
        name=category_name,
        created_at=date.today(),
        account_id = account_id,
        user_id=current_user_id
    )

    db.session.add(category)
    db.session.commit()

    return category_schema.dump(category), 201

# Allow the creator delete the category
@category_bp.route("/delete/<int:category_id>", methods=["DELETE"])
@jwt_required()
def delete_category(category_id):
    # fetch the category
    stmt = db.select(Category).filter_by(id=category_id)
    category = db.session.scalar(stmt)

    if not category:
        return {"error": "Category not found"}, 404
    
    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()

    print(f"cat: {type(category_id)} | cur: {type(current_user_id)}")
    if str(category.user_id) != current_user_id:
        return {"error": "You are not authorised to delete this category"}, 401
    
    # if all checks are passed
    # delete category
    db.session.delete(category)
    db.session.commit()

    return {"message": f"Category '{category_id}' deleted successfully"}, 200