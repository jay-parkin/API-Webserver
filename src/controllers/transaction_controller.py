from datetime import date, datetime

from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from models.account import Account
from models.user_account import UserAccount
from models.transaction import Transaction, TransactionSchema, transaction_schema, transactions_schema
from models.category import Category

from init import db

transaction_bp = Blueprint("transaction", __name__, url_prefix="/transactions")

# Allow all category to be monitored
@transaction_bp.route("/")
def get_all_transactions():
    
    stmt = db.select(Transaction).order_by(Transaction.id)
    transactions = db.session.scalars(stmt)

    return transactions_schema.dump(transactions)

# Allow only admin or contributors to create a new transaction
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
        return {"error": "You are not authorised to create a transaction for this account"}, 401
    
    # Check if the user's role is "Viewer"
    if user_account.role == "Viewer":
        return {"error": "Viewers not authorised to create transactions"}, 401

    # Fetch the category from the body
    body_data = request.get_json()
    category_name = body_data.pop("category_name", None)

    # create a new category instance
    if category_name:
        category = db.session.query(Category).filter_by(name=category_name).first()
        
        if not category:
            # create the category if it doesn't exist
            category = Category(
                name=category_name,
                created_at=date.today(),
                user_id=current_user_id,
                account_id = account_id
            )
            db.session.add(category)
            db.session.commit()
    else:
        category = None

    # get the data from the body of the request
    body_data = TransactionSchema().load(request.get_json(), partial=True)

    # parse the date
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
        category = category,
        user_id = current_user_id
    )

    # Add the new transaction to the session
    db.session.add(transaction)
    db.session.commit()

    return transaction_schema.dump(transaction), 201

# Allow a transactions to be put into a category
@transaction_bp.route("/add_category/<int:transaction_id>", methods=["PUT", "PATCH"])
@jwt_required()
def add_transaction_to_category(transaction_id):
    # fetch transaction
    stmt = db.select(Transaction).filter_by(id=transaction_id)
    transaction = db.session.scalar(stmt)

    if not transaction:
        return {"error": f"Transaction {transaction_id} not found"}, 404

    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()

    # Check to see if the current user is part of the user_account
    user_account = db.session.query(UserAccount).filter_by(
        user_id=current_user_id, account_id=transaction.account_id).first()

    if not user_account:
        return {"error": "You are not authorised to update a transaction for this account"}, 401
    
    if user_account.role == "Viewer":
        return {"error": "Only Admin or Contributor are authorised to update transactions"}, 401

    # Get the data from the body of the request
    body_data = request.get_json()

    # Get the category_id from the request body
    category_id = body_data.get("category_id")

    if not category_id:
        return {"error": "Category ID is required"}, 400

    # Fetch the category
    category = db.session.get(Category, category_id)

    if not category:
        return {"error": f"Category {category_id} not found"}, 404
    
    # Check if the category's account_id matches the transaction's account_id
    if category.account_id != transaction.account_id:
        return {"error": f"Category account_id({category.account_id}) does not match transaction account_id({transaction.account_id})"}, 403

    # Update the transaction with the new category
    transaction.category_id = category_id

    # Commit the session
    db.session.commit()

    # Return the updated transaction
    return transaction_schema.dump(transaction)

# Allow the admin of the account to delete the transaction
@transaction_bp.route("/delete/<int:transaction_id>", methods=["DELETE"])
@jwt_required()
def delete_transaction(transaction_id):
    # fetch transaction
    stmt = db.select(Transaction).filter_by(id=transaction_id)
    transaction = db.session.scalar(stmt)

    if not transaction:
        return {"error:", f"Transaction {transaction_id} not found"}

    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()

    # fetch user account
    # Check to see if the current user is apart of the user_account
    user_account = db.session.query(UserAccount).filter_by(
        user_id=current_user_id, account_id=transaction.account_id).first()

    if not user_account:
        return {"error": "You are not authorised to delete a transaction for this account"}, 401
    
    # Check if the user's role is not admin
    if not user_account.role == "Admin":
        return {"error": "Only Admin are authorised to delete transactions"}, 401

    # If all checks are passed
    # delete account
    db.session.delete(transaction)
    db.session.commit()

    # return success message
    return {"message": f"Transaction '{transaction.id}' deleted successfully"}, 200
    
# Allow the admin or contributor to update transaction information
@transaction_bp.route("/update/<int:transaction_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_transaction(transaction_id):

    # fetch transaction
    stmt = db.select(Transaction).filter_by(id=transaction_id)
    transaction = db.session.scalar(stmt)

    if not transaction:
        return {"error:", f"Transaction {transaction_id} not found"}

    # Get the current user ID from the JWT token
    current_user_id = get_jwt_identity()

    # fetch user account
    # Check to see if the current user is apart of the user_account
    user_account = db.session.query(UserAccount).filter_by(
        user_id=current_user_id, account_id=transaction.account_id).first()

    if not user_account:
        return {"error": "You are not authorised to delete a transaction for this account"}, 401
    
    # Check if the user's role is not admin or contributor
    if user_account.role == "Viewer":
        return {"error": "Only Admin are authorised to delete transactions"}, 401
    
    # get the data from the body of the request
    body_data = TransactionSchema().load(request.get_json(), partial=True)

    # Parse the date from the request body, if provided
    transaction_date_str = body_data.get("date")

    if transaction_date_str:
        try:
            transaction_date = datetime.strptime(transaction_date_str, "%Y-%m-%d").date()
        except ValueError:
            return {"error": "Invalid date format. Date should be in YYYY-MM-DD format"}, 400
        
    else:
        transaction_date = transaction.date

    # update transaction
    transaction.type = body_data.get("type", transaction.type),
    transaction.amount = float(body_data.get("amount", transaction.amount)),
    transaction.date = transaction_date,
    transaction.description = body_data.get("description", transaction.description),
    
    # commit session
    db.session.commit()

    # Return the updated transaction
    return transaction_schema.dump(transaction)