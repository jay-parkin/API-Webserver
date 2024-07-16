from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, And, Regexp, OneOf

VALID_TYPES = ("Income", "Expense")

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)

    # Foreign relation
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    
    user = db.relationship("User", back_populates = "transaction")
    account = db.relationship("Account", back_populates = "transaction")

class TransactionSchema(ma.Schema):

    # a list of nested fields
    user = fields.Nested("UserSchema", only=["name", "email"])
    account = fields.Nested("AccountSchema", exclude=["transaction"])

    # Uses marshmallow to create some validations
    type = fields.String(validate=OneOf(VALID_TYPES))

    class Meta:
        fields = ("id", "type", "amount", "date", "description", "created_at", "account", "user")

# to handle a single user object
transaction_schema = TransactionSchema()

# to handle a list of user objects
transactions_schema = TransactionSchema(many=True)