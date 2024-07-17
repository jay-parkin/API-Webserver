from datetime import date, datetime

from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from models.account import Account, accounts_schema, account_schema
from models.user_account import UserAccount
from models.user import User
from models.transaction import Transaction, transactions_schema, transaction_schema

from init import db

transaction_bp = Blueprint("transaction", __name__, url_prefix="/transactions")

# Allow user to create a new transaction
@transaction_bp.route("/create/<int:account_id>", methods=["POST"])
@jwt_required()
def create_transaction(account_id):
    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()

    # fetch the account from database
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": "Account does not exist"}, 404

    # fetch user account
    # Check to see if the current user is apart of the user_account
    user_account = db.session.query(UserAccount).filter_by(
        user_id=current_user_id, account_id=account_id).first()

    if not user_account:
        return {"error": "You are not authorised to create a transaction for this account"}, 404
    
    # Check if the user's role is "Viewer"
    if user_account.role == "Viewer":
        return {"error": "Viewers not authorised to create transactions"}, 404

    # get the data from the body of the request
    body_data = request.get_json()

     # Parse the date from the request body
    try:
        transaction_date = datetime.strptime(body_data.get("date"), "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date format. Date should be in YYY-MM-DD format"}

    # create a new instance of a transaction
    transaction = Transaction(
        type = body_data.get("type"),
        amount = float(body_data.get("amount")),
        date = transaction_date,
        description = body_data.get("description"),
        created_at = date.today(),
        account = account,
        user_id = current_user_id
    )

    # Add the new transaction to the session
    db.session.add(transaction)
    db.session.commit()

    return transaction_schema.dump(transaction)
