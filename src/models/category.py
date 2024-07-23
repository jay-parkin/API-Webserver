from init import db, ma

from marshmallow import fields
from marshmallow.validate import OneOf

class Category(db.Model):
    # Define the table name
    __tablename__ = "categories"

    # Define the primary key
    id = db.Column(db.Integer, primary_key=True)

    # More attributes(columns)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.Date)

    # Foreign relation
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)

    account = db.relationship("Account", back_populates = "category")
    transaction = db.relationship("Transaction", back_populates = "category")

class CategorySchema(ma.Schema):

    # A list of nested fields
    account = fields.Nested("AccountSchema", only=["id", "name", "type"])
    transaction = fields.List(fields.Nested("TransactionSchema", exclude=["category"]))

    class Meta:
        fields = ("id", "name", "created_at",  "accounts", "transaction")
    
# To handle a single category object
category_schema = CategorySchema()

# To handle multiple category objects
categories_schema = CategorySchema(many=True)