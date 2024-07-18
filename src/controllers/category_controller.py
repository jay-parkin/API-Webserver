
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