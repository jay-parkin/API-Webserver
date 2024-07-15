from datetime import timedelta, date

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models.account import Account, AccountSchema, accounts_schema, account_schema
from init import bcrypt, db

account_bp = Blueprint("account", __name__, url_prefix="/accounts")

@account_bp.route("/all")
def get_all_accounts():
    # fetch all cards but order them in date descending
    stmt = db.select(Account).order_by(Account.created_at.desc())
    accounts = db.session.scalars(stmt)

    return accounts_schema.dump(accounts)