from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from utils import authorise_user

from models.account import Account, AccountSchema, accounts_schema, account_schema
from models.user_account import UserAccount
from models.user import User
from models.transaction import Transaction, transactions_schema
from models.category import Category, categories_schema

from init import db

account_bp = Blueprint("account", __name__, url_prefix="/accounts")

# Allow only accounts associated with the current user to be monitored
@account_bp.route("/all")
@jwt_required()
def get_all_accounts():
    current_user_id = get_jwt_identity()
    
   # Create a query to fetch accounts associated with the current user
    stmt = (
        db.select(Account)
        .join(UserAccount, Account.id == UserAccount.account_id)
        .filter(UserAccount.user_id == current_user_id)
        .order_by(Account.created_at.desc())
    )
    accounts = db.session.scalars(stmt)

    return accounts_schema.dump(accounts)

# Allow all category to be monitored
@account_bp.route("/<int:account_id>/categories", methods=["GET"])
@jwt_required()
@authorise_user(resource_model=Account, 
                resource_param="account_id", 
                attribute_name="id",
                role_required=["Admin", "Contributor", "Viewer"])
def get_all_categories(account_id): 
    # Fetch account
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": "Account not found"}, 404
    
    # Fetch categories associated with this account
    categories = db.session.query(Category).filter_by(account_id=account_id).all()

    if not categories:
        return {"error": "This account has no categories"}, 404

    return categories_schema.dump(categories)

# Allow user to retrive all transactions for account
@account_bp.route("/<int:account_id>/transactions", methods=["GET"])
@jwt_required()
@authorise_user(resource_model=Account, 
                resource_param="account_id", 
                attribute_name="id",
                role_required=["Admin", "Contributor", "Viewer"])
def get_transactions_by_account(account_id):
    # Fetch account
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": "Account not found"}, 404
    
    # Fetch transactions associated with the account
    transactions = db.session.query(Transaction).filter_by(account_id=account_id).all()
    
    if not transactions:
        return {"error": "This account has no Transactions"}, 404
    
    return transactions_schema.dump(transactions)

# Allow user to create a new account
@account_bp.route("/create", methods=["POST"])
@jwt_required()
def create_account():
    # Fetch the current user from the database
    current_user_id = get_jwt_identity()
    current_user = db.session.get(User, current_user_id)

    if not current_user:
        return {"error": "User does not exist"}, 404

    # Get the data from the body of the request
    body_data = account_schema.load(request.get_json())

    # Create a new instance of an account
    account = Account(
        name = body_data.get("name"),
        type = body_data.get("type"),
        created_at = date.today()
    )

    # Create a new instance of UserAccount linking the user as an admin
    user_account = UserAccount(
        role="Admin",
        is_admin=True,
        user_id=current_user_id,
        account=account
    )

    # Add the new account and user_account to the session
    db.session.add(account)
    db.session.add(user_account)
    db.session.commit()

    # Respond
    return account_schema.dump(account), 201

# Allow a user to join another user account
@account_bp.route("/join/<int:account_id>", methods=["POST"])
@jwt_required()
def join_account(account_id):
    # Fetch the current user's ID from JWT token
    current_user_id = get_jwt_identity()

    # Fetch the account
    stmt = db.select(Account).filter_by(id = account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": f"Account with id {account_id} not found"}, 404
   
    # Check if the user is already associated with this account
    existing_user_account = db.session.query(UserAccount).filter_by(
        user_id=current_user_id, account_id=account_id).first()
    
    if existing_user_account:
        return {"error": "You are already a member of this account"}, 400

    # Fetch the user instance
    user = db.session.get(User, current_user_id)

    # Allow use to join
    user_account = UserAccount(
        role = "Viewer",
        user = user,
        account = account
    )

    # Add and commit session
    db.session.add(user_account)
    db.session.commit()

    # Return the created commit
    return account_schema.dump(account), 201 

# Allow the admin of the account to update account name and type
@account_bp.route("/update/<int:account_id>", methods=["PUT", "PATCH"])
@jwt_required()
@authorise_user(resource_model=Account, 
                resource_param="account_id", 
                attribute_name="id",
                role_required=["Admin"])
def update_account(account_id):
    # Fetch the Account from db
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": "Account does not exist"}, 404

    # Get the fields from the body of the request
    body_data = AccountSchema().load(request.get_json(), partial=True)
    
    # Update the account fields
    account.name = body_data.get("name", account.name)
    account.type = body_data.get("type", account.type)

    # Commit session
    db.session.commit()

    # Return the updated account
    return account_schema.dump(account), 200

# Allow the admin of the account to delete the account
@account_bp.route("/delete/<int:account_id>", methods=["DELETE"])
@jwt_required()
@authorise_user(resource_model=Account, 
                resource_param="account_id", 
                attribute_name="id",
                role_required=["Admin"])
def delete_account(account_id):
    # Fetch the Account from db
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)

    if not account:
        return {"error": "Account does not exist"}, 404

    # If all checks are passed
    # Delete account
    db.session.delete(account)
    db.session.commit()

    # Return success message
    return {"message": f"Account '{account.id}' deleted successfully"}, 200