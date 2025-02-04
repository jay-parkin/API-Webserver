from init import db, ma

from marshmallow import fields
from marshmallow.validate import Regexp

class User(db.Model):
    # Define the table name
    __tablename__ = "users"

    # Define the primary key
    id = db.Column(db.Integer, primary_key=True)

    # More attributes (columns)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.Date)
    
    # Foreign relation
    user_account = db.relationship("UserAccount", back_populates = "user", cascade="all, delete-orphan")
    transaction = db.relationship("Transaction", back_populates = "user")

class UserSchema(ma.Schema):

    # A list of nested fields
    user_account = fields.List(fields.Nested("UserAccountSchema", exclude=["user"]))
    transaction = fields.List(fields.Nested("TransactionSchema", exclude=["user"]))
    
    # A list of required fields
    email = fields.String(required=True, 
                               validate=Regexp("^\S+@\S+\.\S+$",
                                               error="Invalid Email Format"))
    password_hash = fields.String(required=True, 
                                  validate=Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", 
                                                  error="Minimum eight characters, at least one letter and one number"))

    class Meta:
        fields = ("id", "name", "email", "password_hash", "created_at")

# To handle a single user object
user_schema = UserSchema(exclude=["password_hash"])

# To handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password_hash"])