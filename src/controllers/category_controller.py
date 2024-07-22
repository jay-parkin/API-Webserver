
from datetime import date, datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from utils import authorise_user

from models.category import Category, CategorySchema, categories_schema, category_schema
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

# Allow only admin or contributors to create a new category
@category_bp.route("/create/<int:account_id>", methods=["POST"])
@jwt_required()
@authorise_user(resource_model=Account, 
                resource_param="account_id", 
                attribute_name="id",
                role_required=["Admin", "Contributor"])
def create_category(account_id):
    
    # fetch the account from database
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": "Account does not exist"}, 404
    
    # Fetch the category from the body
    body_data = request.get_json()
    category_name = body_data.pop("category_name")

    # Check if a category with the same name exists in the same account
    existing_category = db.session.query(Category).filter_by(name=category_name, account_id=account_id).first()
    if existing_category:
        return {"error": "Category with this name already exists in the account"}, 409

    # create a new category instance
    if not category_name:     
        return {"error": "Category name is needed"}, 400   
   
     # create the category if it doesn't exist
    category = Category(
        name=category_name,
        created_at=date.today(),
        account_id = account_id
    )

    db.session.add(category)
    db.session.commit()

    return category_schema.dump(category), 201

# Allow the admin or contributor to update information
@category_bp.route("/update/<int:category_id>", methods=["PUT", "PATCH"])
@jwt_required()
@authorise_user(resource_model=Category, 
                resource_param="category_id", 
                attribute_name="account_id",
                role_required=["Admin", "Contributor"])
def update_category(category_id):

    # fetch category
    stmt = db.select(Category).filter_by(id=category_id)
    category = db.session.scalar(stmt)

    if not category:
        return {"error:", f"Category {category_id} not found"}
    
    # get the data from the body of the request
    body_data = CategorySchema().load(request.get_json(), partial=True)

    category.name = body_data.get("name", category.name)

    # commit session
    db.session.commit()

    # return updated category
    return category_schema.dump(category)

# Allow the creator delete the category
@category_bp.route("/delete/<int:category_id>", methods=["DELETE"])
@jwt_required()
@authorise_user(resource_model=Category, 
                resource_param="category_id", 
                attribute_name="account_id",
                role_required=["Admin"])
def delete_category(category_id):
    # fetch the category
    stmt = db.select(Category).filter_by(id=category_id)
    category = db.session.scalar(stmt)

    if not category:
        return {"error": "Category not found"}, 404

    # if all checks are passed
    # delete category
    db.session.delete(category)
    db.session.commit()

    return {"message": f"Category '{category_id}' deleted successfully"}, 200