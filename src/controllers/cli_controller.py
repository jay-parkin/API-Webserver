from datetime import date

from flask import Blueprint
from init import db, bcrypt

from models.user import User
from models.account import Account
from models.transaction import Transaction
from models.user_account import UserAccount
from models.category import Category

db_commands = Blueprint("db", __name__)

# Cli command used - flask db create
@db_commands.cli.command("create")
def create_tables():
    db.create_all()

    print("Tables have been created...")

# Cli command used - flask db drop
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables have been dropped...")

# Cli command used - flask db seed
@db_commands.cli.command("seed")
def seed_tables():
    # List of user instances
    users = [
        User(
            name="Admin",
            email="admin@example.com",
            password_hash=bcrypt.generate_password_hash("AdminPass123").decode("utf-8"),
            created_at=date.today()
        ),
        User(
            name="Alice",
            email="alice@example.com",
            password_hash=bcrypt.generate_password_hash("AlicePass123").decode("utf-8"),
            created_at=date.today()
        ),
        User(
            name="Bob",
            email="bob@example.com",
            password_hash=bcrypt.generate_password_hash("BobPass123").decode("utf-8"),
            created_at=date.today()
        ),
        User(
            name="Charlie",
            email="charlie@example.com",
            password_hash=bcrypt.generate_password_hash("CharliePass123").decode("utf-8"),
            created_at=date.today()
        )
    ]

    db.session.add_all(users)

    accounts = [
        Account(
            name="Personal Savings",
            type="Savings",
            created_at=date.today()
        ),
        Account(
            name="Vacation Fund",
            type="Savings",
            created_at=date.today()
        ),
        Account(
            name="Business Checking",
            type="Checking",
            created_at=date.today()
        ),
        Account(
            name="Emergency Fund",
            type="Savings",
            created_at=date.today()
        )
    ]

    db.session.add_all(accounts)

    user_accounts = [
        UserAccount(
            role="Admin",
            user=users[0],
            account=accounts[0],
            is_admin=True
        ),
        UserAccount(
            role="Viewer",
            user=users[1],
            account=accounts[1]
        ),
        UserAccount(
            role="Contributor",
            user=users[2],
            account=accounts[2]
        ),
        UserAccount(
            role="Contributor",
            user=users[3],
            account=accounts[3]
        )
    ]

    db.session.add_all(user_accounts)

    categories = [
        Category(
            name="Groceries",
            created_at=date.today(),
            account=accounts[0]
        ),
        Category(
            name="Travel",
            created_at=date.today(),
            account=accounts[1]
        ),
        Category(
            name="Office Supplies",
            created_at=date.today(),
            account=accounts[2]
        ),
        Category(
            name="Healthcare",
            created_at=date.today(),
            account=accounts[3]
        )
    ]

    db.session.add_all(categories)

    transactions = [
        Transaction(
            type="Income",
            amount="2500.00",
            date="2024-07-01",
            description="Salary",
            created_at=date.today(),
            account=accounts[0],
            category=None,
            user=users[0]
        ),
        Transaction(
            type="Expense",
            amount="150.00",
            date="2024-07-05",
            description="Grocery Shopping",
            created_at=date.today(),
            account=accounts[0],
            category=categories[0],
            user=users[0]
        ),
        Transaction(
            type="Income",
            amount="500.00",
            date="2024-07-10",
            description="Freelance Work",
            created_at=date.today(),
            account=accounts[2],
            category=None,
            user=users[2]
        ),
        Transaction(
            type="Expense",
            amount="200.00",
            date="2024-07-12",
            description="Flight Tickets",
            created_at=date.today(),
            account=accounts[1],
            category=categories[1],
            user=users[1]
        ),
        Transaction(
            type="Income",
            amount="1000.00",
            date="2024-07-15",
            description="Bonus",
            created_at=date.today(),
            account=accounts[0],
            category=None,
            user=users[0]
        ),
        Transaction(
            type="Expense",
            amount="75.00",
            date="2024-07-18",
            description="Office Supplies",
            created_at=date.today(),
            account=accounts[2],
            category=categories[2],
            user=users[2]
        ),
        Transaction(
            type="Expense",
            amount="300.00",
            date="2024-07-20",
            description="Doctor Visit",
            created_at=date.today(),
            account=accounts[3],
            category=categories[3],
            user=users[3]
        ),
        Transaction(
            type="Income",
            amount="600.00",
            date="2024-07-25",
            description="Sold Bicycle",
            created_at=date.today(),
            account=accounts[1],
            category=None,
            user=users[1]
        )
    ]

    db.session.add_all(transactions)

    db.session.commit()

    print("Tables are now seeded...")
