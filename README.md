# API Webserver: Income & Expense Tracker

## R1: Problem Statement

Managing personal and shared finances can be challenging, especially for couples who need to keep track of joint income and expenses. <br>
Many existing financial management tools offer comprehensive budget planning features, but they often fall short in providing a simple and efficient way to track financial transactions among multiple users. <br>
This can lead to difficulties in maintaining shared finances, resulting in misunderstandings or conflicts over financial matters.

Financial stress is a significant cause of tension in relationships. Studies show that money problems are a leading cause of stress and a strong predictor of marital conflict and divorce. For instance, Relationships Australia found that financial stress is a major factor in relationship breakdowns, with money-related issues being a stronger predictor of divorce than other marital disagreements ([AusUnity](https://www.australianunity.com.au/wellbeing/money-and-finances/how-to-talk-about-money-in-a-relationship)).

Personally, I've tried budgeting apps, but nothing suited what I needed, leaving my wife and me to compare expenses at the end of the week. This left holes in our budget. According to Australian Unity, financial compatibility and regular communication about money are essential for maintaining a healthy relationship. Misaligned financial goals and habits can lead to significant conflicts and even separation ([AusUnity](https://www.australianunity.com.au/wellbeing/money-and-finances/how-to-talk-about-money-in-a-relationship)).

I've spent many hours on the internet in search of an expense tracker that can be shared between couples so that no expense is left untracked. The National Australia Bank reported a rise in consumer anxiety over finances, emphasising the need for effective financial management tools that cater specifically to couples' needs ([Women's Agenda](https://womensagenda.com.au/latest/is-financial-stress-affecting-your-relationship-here-are-5-things-you-can-do/)).<br>

### Solution

The Income and Expense Tracker API is here to make managing money easier for couples. It simplifies how you track your finances, allowing you to effortlessly record income and expenses.
It also provides a user-friendly solution for tracking financial transactions, focusing on recording income and expenses while supporting the sharing of transaction accounts between partners. <br>

<i>Property Update</i> emphasises that financial management apps can save you time by automating tasks, give you real-time updates on your spending, and offer all-in-one management tools. For couples, this means both partners can stay up-to-date on their finances, which helps promote better cooperation and reduces the chances of conflicts ([Property Update](https://propertyupdate.com.au/the-ultimate-guide-to-budgeting-as-a-couple/)).

Here’s how the app will address the problem:

#### Simplified Financial Tracking

The API makes it easy to record income and expenses, capturing key details like transaction type, amount, date, and description. This straightforward approach helps couples keep accurate financial records without the hassle of a complex budget planner.

#### Shared Accounts

A standout feature is the ability to share transaction accounts with multiple users, perfect for couples managing joint finances. Both partners can view and record transactions, encouraging transparency and collaboration.

#### User Roles and Permissions

The API allows for assigning different roles within shared accounts, such as admin, contributor, or viewer. This role-based access control ensures each partner has the right level of access and permissions, ensuring security.

#### Categorisation & Organisation

Users can categorise transactions to better organise their financial data. This helps couples understand their spending patterns and income sources, making financial planning and decision-making easier.

#### Real-time Collaboration

With multiple users able to interact with the same account in real-time, the API ensures all financial data is up-to-date and accessible to both partners. This eliminates delays and ensures everyone is on the same page about their financial status.

The Income and Expense Tracker API addresses the common challenges couples face in managing their joint finances. By focusing on simplicity, shared account functionality, user roles, categorisation, and real-time collaboration, the API provides a solution for financial organisation, and cooperation. This approach makes it easier for couples to manage their income and expenses, reducing the financial misunderstandings.

## R2: Task Allocation and Tracking

To ensure thorough task management and progress tracking, I use [Atlassian's Trello](https://trello.com/home). <br>
Trello allows me to organise tasks visually and track their status through various stages of completion.

1. <b>Task Allocation</b>

   - <b>Task Creation:</b> I create tasks as individual Trello cards, each representing a specific task that needs completion.
   - <b>Details and Deadlines:</b> Each card includes a detailed description, relevant attachments and checklists. This keeps me organised and ensures I have all necessary information to complete the task.

2. <b>Tracking Progress</b>

   - <b>Backlog:</b> This list contains all tasks that need to be done eventually but are not yet prioritised. It's future tasks that I can move to "To Do" when ready to start working on them.

   - <b>README.md:</b> This will list all of the updates/changes I need to make to the readme.md file of this project. Card from here will be moved into 'Doing' once started.

   - <b>API Routes/Endpoints:</b> Basing this list off work that needs to be done in Insomnia.

   - <b>To Do:</b> This list includes all tasks that need starting. New tasks are added here, giving a clear view of what's next.

   - <b>Doing:</b> Once I start working on a task, I move its card from "To Do" to "Doing." This helps me focus on current tasks and manage my workflow efficiently.

   - <b>Done:</b> Completed tasks go into the "Done" list, providing a sense of accomplishment and a clear record of finished work.

   - <b>Stuck:</b> If a task encounters an issue or can't proceed, it goes to the "Stuck" list. This helps me quickly spot and resolve bottlenecks.

3. <b>Communication and Updates</b>

   - <b>Notes:</b> I add notes to each card for updates, recording important information, or documenting task-related issues.

   - <b>Notifications:</b> Trello notifies me about approaching deadlines and any updates or changes to cards, helping me stay informed and manage time effectively.

4. <b>Review</b>

   - <b>Regular Review:</b> I regularly review task statuses and project progress to stay on track and adjust my workflow as needed.

   - <b>Board Review:</b> Periodically, I review the Trello board to ensure tasks move smoothly. This early identification of delays or issues allows prompt resolution.

<br>

Live link: [API Webserver: Income & Expense Tracker](https://trello.com/b/Xe5Zb2LJ)

<details>
   <summary>Trello Planning: Screenshots</summary>
   <p align="center">First Week</p>
<p align="center">
   <img src="docs/planning/trello/planning_stage_01.JPG">
   <img src="docs/planning/trello/planning_stage_02.JPG">
</p>
<p align="center">Second Week</p>
<p align="center">
   <img src="docs/planning/trello/planning_stage_15.JPG">
   <img src="docs/planning/trello/planning_stage_16.JPG">
   <img src="docs/planning/trello/planning_stage_17.JPG">
</p>
<p align="center">Third Week</p>
<p align="center">
   <img src="docs/planning/trello/planning_stage_18.JPG">
   <img src="docs/planning/trello/planning_stage_19.JPG">
</p>
</details>

<details>
   <summary>Card Planning: Screenshots</summary>
<p align="center">
   <img src="docs/planning/trello/cards/card_r01.JPG">
   <img src="docs/planning/trello/cards/card_r02.JPG">
   <img src="docs/planning/trello/cards/card_r03.JPG">
   <img src="docs/planning/trello/cards/card_r04.JPG">
   <img src="docs/planning/trello/cards/card_r06.JPG">
   <img src="docs/planning/trello/cards/card_r05.JPG">
   <img src="docs/planning/trello/cards/card_r07.JPG">
   <img src="docs/planning/trello/cards/card_r08.JPG">
</p>
</details>

## R3: Third-party Services, Packages and Dependencies

<b>[SQLAlchemy](https://pypi.org/project/SQLAlchemy/)</b>

```bash
pip install SQLAlchemy
```

<b>Purpose:</b> SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides tools for database schema management and query construction, allowing developers to work with relational databases using Python objects rather than writing raw SQL queries.

<b>Usage:</b> It is used to manage database schemas, execute queries, and perform CRUD operations. SQLAlchemy supports multiple databases like PostgreSQL, MySQL, SQLite, etc.

<b>[Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)</b>

```bash
pip install Flask-SQLAlchemy
```

<b>Purpose:</b> Flask-SQLAlchemy is an extension for Flask that integrates SQLAlchemy with Flask applications. It provides a higher-level abstraction to manage database connections and ORM functionalities within a Flask app.

<b>Usage:</b> Simplifies database management in Flask by providing easy access to SQLAlchemy features and better integration with Flask's application context.

<b>[marshmallow-sqlalchemy](https://pypi.org/project/marshmallow-sqlalchemy/)</b>

```bash
pip install marshmallow-sqlalchemy
```

<b>Purpose:</b> This library extends Marshmallow, which is a library for object serialisation and deserialisation, to work specifically with SQLAlchemy ORM models. It facilitates the conversion of SQLAlchemy models to and from JSON.

<b>Usage:</b> Helps in serialising SQLAlchemy models into JSON format for API responses and deserialising JSON into SQLAlchemy models for processing incoming data.

<b>[flask-marshmallow](https://pypi.org/project/flask-marshmallow/)</b>

```bash
pip install flask-marshmallow
```

<b>Purpose:</b> Flask-Marshmallow integrates Marshmallow with Flask, providing a convenient way to serialise and deserialise data within Flask applications.

<b>Usage:</b> It combines Flask with Marshmallow's features for handling JSON serialisation and deserialisation, often used in Flask API endpoints.

<b>[Flask-Bcrypt](https://pypi.org/project/Flask-Bcrypt/)</b>

```bash
pip install Flask-Bcrypt
```

<b>Purpose:</b> Flask-Bcrypt is an extension that integrates bcrypt hashing with Flask applications. It provides a way to hash passwords securely using the bcrypt algorithm.

<b>Usage:</b> Typically used for password hashing and verification, enhancing security in authentication processes.

<b>[psycopg2](https://pypi.org/project/psycopg2/)</b>

```bash
pip install psycopg2
```

<b>Purpose:</b> Psycopg2 is a PostgreSQL adapter for Python, allowing Python applications to connect to and interact with PostgreSQL databases.

<b>Usage:</b> Provides the necessary interface for executing SQL commands and managing database connections with PostgreSQL.

<b>[psycopg2-binary](https://pypi.org/project/psycopg2-binary/)</b>

```bash
pip install psycopg2-binary
```

<b>Purpose:</b> Psycopg2-binary is a binary distribution of psycopg2 that includes precompiled binaries to simplify installation and avoid the need for compilation.

<b>Usage:</b> Provides the same functionality as psycopg2 but simplifies the installation process by including prebuilt binaries.

<br>

These can be found in the `requirements.txt` and can be installed with the following command:

```bash
pip install -r requirements.txt
```

<i>Note: In most modern setups where Python 2 is no longer in use, pip should work for Python 3.x as well. However, if you're unsure or have both Python 2 and 3 installed, using pip3 ensures that you're installing packages for Python 3.x.</i>

## R4: Benefits and Drawbacks of PostgreSQL

<b>Overview of Relational Database Systems (RDBMS)</b><br>
Relational Database Systems are databases that store data in a structured format, using rows and columns. They are based on the relational model introduced by E.F. Codd in the 1970s. Data is organised into tables, and relationships between data items are managed through foreign keys and indexes. SQL (Structured Query Language) is the standard language used to interact with RDBMS.

<b>Structured Data Storage</b>

- Data is organised into tables with predefined schemas.<br>
- Tables are made up of rows (records) and columns (fields), which helps in maintaining data consistency.

<b>Data Integrity</b>

- <b>ACID Transactions:</b> Ensures Atomicity, Consistency, Isolation, and Durability, which are crucial for reliable transaction processing.
- <b>Constraints:</b> Enforces data integrity through primary keys, foreign keys, unique constraints, and check constraints.

<b>Normalisation</b>

- <b>Normalisation:</b> The process of organising data to reduce redundancy and improve data integrity. This involves dividing tables into smaller, related tables.

<b>SQL Support</b>

- <b>Query Language:</b> Provides a powerful and standardised way to query and manipulate data using SQL.

<b>Indexing</b>

- <b>Indexes:</b> Improve the speed of data retrieval operations on tables.

<b>Relationships:</b>

- <b>Joins:</b> Facilitate complex queries by allowing the combination of data from multiple tables based on related columns.

### Benefits

1. <b>Advanced Features</b>:

   - <b>ACID Compliance</b>: Ensures reliable transactions and data integrity.
   - <b>Complex Queries</b>: Supports complex queries with SQL, including sub-selects, joins, and window functions.
   - <b>Full-Text Search</b>: Provides built-in full-text search capabilities.
   - <b>JSON Support</b>: Allows storing and querying JSON data efficiently.

2. <b>Extensibility</b>:

   - <b>Custom Data Types</b>: You can define your own data types and functions.
   - <b>Extensions</b>: Supports extensions like PostGIS for spatial data and others for added functionality.

3. <b>Scalability</b>:

   - <b>Large Data Volumes</b>: Handles large databases efficiently.
   - <b>Concurrency Control</b>: Uses Multi-Version Concurrency Control (MVCC) to handle high concurrency with minimal locking.

4. <b>Standards Compliance</b>:

   - <b>SQL Compliance</b>: Adheres closely to SQL standards, making it easier to migrate from other SQL databases.
   - <b>Data Integrity</b>: Enforces data integrity constraints such as foreign keys, unique constraints, and check constraints.

5. <b>Open Source</b>:

   - <b>Cost-Effective</b>: No licensing costs associated with the software.
   - <b>Community Support</b>: Large community with extensive documentation, forums, and third-party tools.

6. <b>Performance Tuning</b>:
   - <b>Indexing Options</b>: Offers various indexing strategies to optimise performance.
   - <b>Query Optimisation</b>: Advanced query planner and optimiser.

### Drawbacks

1. <b>Complexity</b>:

   - <b>Configuration</b>: May require fine-tuning and complex configuration for optimal performance.
   - <b>Learning Curve</b>: Advanced features and extensibility can lead to a steeper learning curve.

2. <b>Performance Overheads</b>:

   - <b>Write-Heavy Workloads</b>: While PostgreSQL handles read-heavy workloads well, write-heavy workloads might experience some performance overhead due to MVCC and other features.

3. <b>Resource Consumption</b>:

   - <b>Memory Usage</b>: Can be resource-intensive, especially with complex queries and large datasets.
   - <b>Disk Space</b>: May use more disk space due to its support for extensive features and indexing.

4. <b>Replication and Clustering</b>:

   - <b>Built-in Options</b>: While PostgreSQL supports replication, clustering solutions are not as straightforward as those in some commercial databases.

5. <b>Tooling and Ecosystem</b>:
   - <b>Third-Party Tools</b>: Some advanced features might not have as rich a set of third-party tools compared to commercial databases.

Relational database systems, like PostgreSQL, are great for handling structured data while ensuring data integrity, flexibility, and strong query capabilities. They work well for a lot of different applications, but as your data grows in size and complexity, you'll need to manage and optimise them carefully.

## R5: Object-Relational Mapping (ORM)

SQLAlchemy is a powerful ORM system, which was used in this application to interact with the database in an object-oriented way.

### Features of SQLAlchemy

1. <b>Declarative Mapping:</b>

   - Allows defining classes mapped to database tables, using a declarative base. This makes the ORM models intuitive and easy to read.

2. <b>SQL Expression Language:</b>

   - Provides a way to write SQL queries using Python constructs, offering both flexibility and the ability to perform complex queries.

3. <b>Session Management:</b>

   - Manages transactions and connections to the database through a session system. This simplifies the process of committing changes, rolling back transactions, and querying the database.

4. <b>Relationships and Joins:</b>

   - Simplifies the definition of relationships between tables. Supports one-to-many, many-to-one, and many-to-many relationships, allowing for complex data models.

5. <b>Schema Definition and Migration:</b>

   - SQLAlchemy allows you to define your database schema using a declarative base class. This enables you to represent database tables as Python classes, making your code more readable and maintainable.

6. <b>Validation and Serialisation:</b>

   - Integrates with Marshmallow for data validation and serialisation, making it easy to convert between database objects and Python dictionaries/JSON

### Purpose of SQLAlchemy

The primary purpose of SQLAlchemy is to bridge the gap between the object-oriented programming world of Python and the relational database management system (PostgreSQL in this case). It allows developers to interact with the database using Python objects and methods instead of writing raw SQL queries.

### Functionalities Provided by SQLAlchemy

1. <b>Database Model Definition:</b>

   - I have defined models for `User`, `Account`, `UserAccount`, `Transaction`, and `Category` using SQLAlchemy. Each model class corresponds to a database table.

   Model Definition: User

   ```python
   class User(db.Model):
      # Define the table name
      __tablename__ = "users"

      # Define the primary key
      id = db.Column(db.Integer, primary_key=True)

      # More attributes (columns)
      name = db.Column(db.String(100))
      email = db.Column(db.String(100), nullable=False, unique=True)
      password_hash = db.Column(db.String(100), nullable=False)
      created_at = db.Column(db.Date)

      # Foreign relation
      user_account = db.relationship("UserAccount", back_populates = "user", cascade="all, delete-orphan")
      transaction = db.relationship("Transaction", back_populates = "user")
   ```

   <br>

2. <b>Relationships Management:</b>

   - SQLAlchemy simplifies the management of relationships between tables. For instance, a `User` can have multiple `UserAccount` and `Transaction` records.

   <summary>Foreign Relation: User</summary>

   ```python
   # Foreign relation
   user_account = db.relationship("UserAccount", back_populates = "user", cascade="all, delete-orphan")
   transaction = db.relationship("Transaction", back_populates = "user")
   ```

3. <b>Querying the Database:</b>

   - Provides an easy way to query the database. For example, fetching all accounts for a user, joining tables, and applying filters is done seamlessly with SQLAlchemy.

   <summary>DB Query: Account</summary>

   ```python
   # Create a query to fetch accounts associated with the current user
   stmt = (
      db.select(Account)
      .join(UserAccount, Account.id == UserAccount.account_id)
      .filter(UserAccount.user_id == current_user_id)
      .order_by(Account.created_at.desc())
   )

   # Retrieve a list of scalar values from the result
   accounts = db.session.scalars(stmt)

   # Respond
   return accounts_schema.dump(accounts)
   ```

4. <b>Session Management:</b>

   - Handles sessions to manage transactions, ensuring that operations are atomic and the database state is consistent.

   <summary>DB Query: Account</summary>

   ```python
   # Add the new account and user_account to the session
   db.session.add(account)
   db.session.add(user_account)
   db.session.commit()

   # Respond
   return account_schema.dump(account), 201
   ```

5. <b>Data Validation and Serialisation:</b>

   - With Marshmallow schemas, SQLAlchemy models are validated and serialised efficiently. This is crucial for ensuring data integrity and converting data to/from JSON.

   <summary>Data Validation: Account</summary>

   ```python
    # Get the data from the body of the request
    body_data = account_schema.load(request.get_json())

    # Create a new instance of an account
    account = Account(
        name = body_data.get("name"),
        type = body_data.get("type"),
        created_at = date.today()
    )
   ```

6. CRUD Operations:

   - CRUD Operations refer to the basic operations for managing data in a database. They stand for `Create`, `Read`, `Update`, and `Delete`.

     1. <b>Create:</b> Adds new records to the database.
     2. <b>Read:</b> Read/Retrieves records from the database.
     3. <b>Update:</b> Modifies existing records in the database.
     4. <b>Delete:</b> Removes records from the database.

   In SQLAlchemy, these operations are typically facilitated using a session object.

   <summary>CRUD: Example</summary>

   ```python
   # Create a new account and add it to the database
   new_account = Account(name="John Doe", type="Checking", created_at=date.today())
   db.session.add(new_account)
   db.session.commit()

   # Read/Retrieve an account by its ID
   account_id = 1
   account = Account.query.get(account_id)

   # Update the name of an existing account
   if account:
      account.name = "Jane Doe"
      db.session.commit()

   # Delete an account from the database
   if account:
      db.session.delete(account)
      db.session.commit()
   ```

SQLAlchemy in an application serves as a powerful and flexible ORM, allowing for the definition of database schemas as Python classes, management of relationships, execution of complex queries, and efficient handling of transactions. Its integration with Marshmallow further enhances data validation and serialisation, making it an indispensable tool for developing robust and maintainable applications.

## R6: Entity Relationship Diagram: Design

### User

<b>Attributes:</b>

- `id` (Integer)
- `user_name` (String: max length 100)
- `user_email`(String: max length 100, unique, not nullable)
- `password_hash`(String: max length 100, not nullable)
- `created_at` (Date)

<b>Primary Key:</b> `id`<br>
<b>Relationships</b>

- Each User can have multiple UserAccount associations (one-to-many relationship).
- Each User can have multiple Transaction entries (one-to-many relationship).

### Account

<b>Attributes:</b>

- `id` (Integer)
- `account_name` (String: max length 100, not nullable)
- `account_type` (String: max length 100, not nullable)
- `created_at` (Date)

<b>Primary Key:</b> `id`<br>
<b>Relationships</b>

- Each Account can have multiple UserAccount associations (one-to-many relationship).
- Each Account can have multiple Category entries (one-to-many relationship).
- Each Account can have multiple Transaction entries (one-to-many relationship).

### UserAccount

<b>Attributes:</b>

- `id` (Integer)
- `role` (String: max length 100, not nullable)
- `is_admin` (Boolean, default False)
- `created_at` (Date)

<b>Primary Key:</b> `id` <br>
<b>Foreign Keys:</b>

- `user_id` (Foreign Key referencing User.id, not nullable)
- `account_id` (Foreign Key referencing Account.id, not nullable)

<b>Relationships</b>

- Each UserAccount belongs to one User (many-to-one relationship).
- Each UserAccount belongs to one Account (many-to-one relationship).
- This table creates a many-to-many relationship between User and Account with additional attributes like role.

### Transaction

<b>Attributes:</b>

- `id` (Primary Key, Integer)
- `type` (String: max length 100, not nullable)
- `amount` (Numeric: precision 10, scale 2, not nullable)
- `date` (Date)
- `description` (String: max length 100)
- `created_at` (Date)

<b>Primary Key:</b> `transaction_id`<br>
<b>Foreign Keys:</b>

- `category_id` (Foreign Key referencing Category.id)
- `account_id` (Foreign Key referencing Account.id, not nullable)
- `user_id` (Foreign Key referencing User.id, not nullable)

<b>Relationships</b>

- Each Transaction belongs to one User (many-to-one relationship).
- Each Transaction belongs to one Account (many-to-one relationship).
- Each Transaction belongs to one Category (many-to-one relationship).

### Category

<b>Attributes:</b>

- `id` (Integer)
- `name` (String: max length 100, not nullable)
- `created_at` (Date)

<b>Primary Key:</b> `id`<br>
<b>Foreign Keys:</b>

- `account_id` (Foreign Key referencing Account.id, not nullable)

<b>Relationships</b>

- Each Category belongs to one Account (many-to-one relationship).
- Each Category can have multiple Transaction entries (one-to-many relationship).

### ERD Summary

<b>User</b><br>
Attributes: id, name, email, password_hash, created_at<br>
Primary Key: id<br>
Relationships: One-to-many with UserAccount, One-to-many with Transaction<br>

<b>Account</b><br>
Attributes: id, name, type, created_at<br>
Primary Key: id<br>
Relationships: One-to-many with UserAccount, One-to-many with Category, One-to-many with Transaction<br>

<b>Category</b><br>
Attributes: id, name, created_at<br>
Primary Key: id<br>
Relationships: Many-to-one with Account, One-to-many with Transaction<br>

<b>Transaction</b><br>
Attributes: id, type, amount, date, description, created_at, user_id, account_id, category_id<br>
Primary Key: id<br>
Relationships: Many-to-one with User, Many-to-one with Account, Many-to-one with Category<br>

<details>
   <summary>Entity Relationship Diagram: Image</summary>
<p align="center">Stage Design: Pitch
   <img src="docs/planning/erd/ExpenseERD 240708.jpg">
</p>
<p align="center">Stage Design: 01
   <img src="docs/planning/erd/ExpenseERD 240717.jpg">
</p>
<p align="center">Stage Design: 02
   <img src="docs/planning/erd/ExpenseERD 240720.jpg">
</p>
<p align="center">Stage Design: Final
   <img src="docs/planning/erd/ExpenseERD 240722.jpg">
</p>
</details>
