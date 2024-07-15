from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp

class User(db.Model):
    # define the table name
    __tablename__ = "users"

    # define the primary key
    id = db.Column(db.Integer, primary_key=True)

    # more attributes (columns)
    name = db.Column(db.String(100))
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date)
    
    # Foreign relation
    transactions = db.relationship("Transaction", back_populates = "user",cascade="all, delete")

class UserSchema(ma.Schema):

    # a list of nested fields
    transactions = fields.List(fields.Nested('TransactionSchema', exclude=["user"]))

    # a list of required fields
    email = fields.String(required=True, 
                               validate=Regexp("^\S+@\S+\.\S+$",
                                               error="Invalid Email Format"))
    password_hash = fields.String(required=True, 
                                  validate=Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", 
                                                  error="Minimum eight characters, at least one letter and one number"))

    class Meta:
        fields = ("id", "name", "email", "password_hash", "created_at")

# to handle a single user object
user_schema = UserSchema(exclude=["password_hash"])

# to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password_hash"])