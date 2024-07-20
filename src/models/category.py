from init import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

class Category(db.Model):
    # define the table name
    __tablename__ = "categories"

    # define the primary key
    id = db.Column(db.Integer, primary_key=True)

    # more attributes(columns)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.Date)

    #Foreign relation
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)

    user = db.relationship("User", back_populates = "category")
    account = db.relationship("Account", back_populates = "category")
    transaction = db.relationship("Transaction", back_populates = "category")

class CategorySchema(ma.Schema):

    # a list of nested fields
    user = fields.Nested("UserSchema", only=["name", "email"])
    account = fields.Nested("AccountSchema", only=["id", "name", "type"])
    transaction = fields.List(fields.Nested("TransactionSchema", exclude=["category"]))

    class Meta:
        fields = ("id", "name", "created_at", "user", "accounts", "transaction")
    
# to handle a single category object
category_schema = CategorySchema()

# to handle multiple category objects
categories_schema = CategorySchema(many=True)