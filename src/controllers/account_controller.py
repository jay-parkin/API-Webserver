from datetime import timedelta, date

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models.account import Account, accounts_schema, account_schema
from init import bcrypt, db

account_bp = Blueprint("account", __name__, url_prefix="/accounts")

# Allow all accounts to be monitored
@account_bp.route("/all")
def get_all_accounts():
    
    stmt = db.select(Account).order_by(Account.created_at.desc())
    accounts = db.session.scalars(stmt)

    return accounts_schema.dump(accounts)

# # Allow user to create a new account
# @account_bp.route("/create", methods=["POST"])
# @jwt_required()
# def create_account():
#     # get the data from the body of the request
#     body_data = account_schema.load(request.get_json())

#     #create a new card model instance
#     card = Card(
#         title = body_data.get("title"),
#         description = body_data.get("description"),
#         date = date.today(),
#         status = body_data.get("status"),
#         priority = body_data.get("priority"),
#         user_id = get_jwt_identity() # pull token information about the user
#     )

#     # Create a new instance of an account
#     account = Account(
#         name = body_data.get("name"),
#         type = body_data("type"),
#         created_at = date.today()
#         # needs the userAccount
#     )

#     #add and commit to DB
#     db.session.add(card)
#     db.session.commit()

#     # respond
#     return card_schema.dump(card)