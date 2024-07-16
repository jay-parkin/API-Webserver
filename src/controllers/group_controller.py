from datetime import timedelta, date

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models.group import Group, GroupSchema, groups_schema, group_schema
from models.user import User
from init import bcrypt, db

group_bp = Blueprint("group", __name__, url_prefix="/groups")

# Allow all groups to be monitored
@group_bp.route("/all")
def get_all_groups():

    stmt = db.select(Group).order_by(Group.id)
    groups = db.session.scalars(stmt)

    return groups_schema.dump(groups)

# Allowing the user to leave a group
@group_bp.route("/<int:group_id>", methods=["DELETE"])
@jwt_required()
def delete_group(group_id):
    # fetch the group from the db with the id
    stmt = db.select(Group).filter_by(id = group_id)
    group = db.session.scalar(stmt)

    # if exists?
    if group:
        # delete/leave group
        db.session.delete(group)
        db.session.commit()

        # return success message
        return {"message": f"Group '{group.id}' deleted successfully"}
    # else
    else:
        # return an error saying the comment does not exist
        return {"error": f"Group with id {group_id} not found"}, 404
    
# Allow the admin to update user roles
@group_bp.route("/update/<int:group_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_role(group_id):

    # get fields from body of the request
    body_data = GroupSchema().load(request.get_json(), partial=True)

    # fetch the group from db
    stmt = db.select(Group).filter_by(id=group_id)
    group = db.session.scalar(stmt)

    # Fetch the current user from the database
    current_user_id = get_jwt_identity()
    current_user = db.session.get(User, current_user_id)

    if not current_user:
        return {"error": "User does not exist"}, 404

    # Get fields from the body of the request
    body_data = GroupSchema().load(request.get_json(), partial=True)

    # Fetch the group from the database
    stmt = db.select(Group).filter_by(id=group_id)
    group = db.session.scalar(stmt)

    if not group:
        return {"error": "Group does not exist"}, 404

    # Check if the current user is an admin in the same account
    admin_stmt = db.select(Group).filter_by(user_id=current_user_id, account_id=group.account_id, is_admin=True)
    admin_group = db.session.scalar(admin_stmt)

    if not admin_group:
        return {"error": "You are not authorised to update roles for this group"}, 403

    # Update the fields
    group.role = body_data["role"] or group.role
    group.is_admin = body_data["is_admin"] or group.is_admin

    # Commit to the database
    db.session.commit()

    # Return a response
    return group_schema.dump(group), 200
    
