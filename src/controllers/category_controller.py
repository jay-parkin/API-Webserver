
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.category import Category, categories_schema, category_schema
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