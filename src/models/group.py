from init import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_TYPES = ("Admin", "Contributor", "Viewer")

class Group(db.Model):
    # define the table name
    __tablename__ = "groups"

    # defin the primary key
    id = db.Column(db.Integer, primary_key=True)

    # more attributes(columns)
    role = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Foreign relation
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)

    user = db.relationship("User", back_populates = "group")
    account = db.relationship("Account", back_populates = "group")

class GroupSchema(ma.Schema):
    # a list nested fields
    user = fields.Nested("UserSchema", only=["name", "email"])
    account = fields.Nested("AccountSchema", exclude=["group"])

    # Uses marshmallow to create some validations
    role = fields.String(validate=OneOf(VALID_TYPES))

    class Meta:
        fields = ("id", "role", "is_admin", "user", "account")

# to handle a single user object
group_schema = GroupSchema()

# to handle a list of user objects
groups_schema = GroupSchema(many=True)