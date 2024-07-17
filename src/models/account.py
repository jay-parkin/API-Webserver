from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf

VALID_TYPES = ("Regular Savings", "Personal Checking", "Business Checking", "Joint Account", 
               "Investment", "Retirement", "Credit", "Emergency Fund", "Health Savings", 
               "Education Savings", "Vacation Fund")


class Account(db.Model):
    # define the table name
    __tablename__ = "accounts"

    # define the primary key
    id = db.Column(db.Integer, primary_key=True)

    # more attributes (columns)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date)

    user_account = db.relationship("UserAccount", cascade="all, delete-orphan", back_populates="account")
    transaction = db.relationship("Transaction", cascade="all, delete-orphan", back_populates="account")

class AccountSchema(ma.Schema):

    # a list of nested fields
    user_account = fields.List(fields.Nested("UserAccountSchema", exclude=["account"]))
    transaction = fields.List(fields.Nested("TransactionSchema", exclude=["account"]))
    
    # Uses marshmallow to create some validations
    name = fields.String(required = True, validate = And(
        Length(min = 2, error = "Title must be at least 2 characters long"),
        Regexp("^[A-Za-z0-9 ]+$", error = "Title must have aplhanumerics characters only")
    ))

    type = fields.String(validate=OneOf(VALID_TYPES))

    class Meta:
        fields = ("id", "name", "type", "created_at", "user_account", "transaction")

# to handle a single user object
account_schema = AccountSchema()

# to handle a list of user objects
accounts_schema = AccountSchema(many=True)