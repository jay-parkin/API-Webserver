from datetime import date

from flask import Blueprint
from init import db, bcrypt

from models.user import User
from models.account import Account
from models.transaction import Transaction
from models.user_account import UserAccount

db_commands = Blueprint("db", __name__)

# cli command used - flask db create
@db_commands.cli.command("create")
def create_tables():
    db.create_all()

    print("Tables have been created...")

# cli command used - flask db drop
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables have been dropped...")

# cli command used - flask db seed
@db_commands.cli.command("seed")
def seed_tables():

    # list of user instances
    users = [
        User(
            name = "Admin",
            email = "admin@email.com",
            password_hash = bcrypt.generate_password_hash("123456AA").decode("utf-8"),
            created_at = date.today()
        ),
        User(
            name = "User 1",
            email = "user1@email.com",
            password_hash = bcrypt.generate_password_hash("123456AA").decode("utf-8"),
            created_at = date.today()
        ),
        User(
            name = "User 2",
            email = "user2@email.com",
            password_hash = bcrypt.generate_password_hash("123456AA").decode("utf-8"),
            created_at = date.today()
        ),
        User(
            name = "User 3",
            email = "user3@email.com",
            password_hash = bcrypt.generate_password_hash("123456AA").decode("utf-8"),
            created_at = date.today()
        )
    ]

    db.session.add_all(users)

    accounts = [
        Account(
            name = "Account 1",
            type = "Credit",
            created_at = date.today()
        ),

        Account(
            name = "Account 2",
            type = "Vaction Fund",
            created_at = date.today()
        ),

        Account(
            name = "Account 3",
            type = "Regular Savings",
            created_at = date.today()
        ),

        Account(
            name = "Account 4",
            type = "Personal Checking",
            created_at = date.today()
        )
    ]

    db.session.add_all(accounts)

    user_accounts = [
        UserAccount(
            role = "Admin",
            user = users[0],
            account = accounts[1],
            is_admin = True
        ),
        UserAccount(
            role = "Viewer",
            user = users[1],
            account = accounts[1]
        ),
        UserAccount(
            role = "Contributor",
            user = users[3],
            account = accounts[1]
        ),
    ]

    db.session.add_all(user_accounts)

    transactions = [
        Transaction(
            type = "Income",
            amount = "1200.00",
            date = "2024-07-13",
            description = "Wage or Salary",
            created_at = date.today(),
            account = accounts[2],
            user = users[0]
        ),
        Transaction(
            type = "Expense",
            amount = "232.00",
            date = "2024-07-02",
            description = "New Bed",
            created_at = date.today(),
            account = accounts[3],
            user = users[0]
        ),
        Transaction(
            type = "Income",
            amount = "357.00",
            date = "2024-07-15",
            description = "Yard work",
            created_at = date.today(),
            account = accounts[1],
            user = users[1]
        ),
        Transaction(
            type = "Income",
            amount = "455.00",
            date = "2024-03-25",
            description = "Investment",
            created_at = date.today(),
            account = accounts[2],
            user = users[0]
        ),
        Transaction(
            type = "Expense",
            amount = "156.00",
            date = "2024-05-30",
            description = "Shopping",
            created_at = date.today(),
            account = accounts[2],
            user = users[0]
        ),
        Transaction(
            type = "Income",
            amount = "500.00",
            date = "2024-07-15",
            description = "Sold Tredmill",
            created_at = date.today(),
            account = accounts[1],
            user = users[1]
        )
    ]

    db.session.add_all(transactions)

    db.session.commit()

    print("Tables are now seeded...")