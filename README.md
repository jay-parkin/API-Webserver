# API Webserver: Income & Expense Tracker

## R1: Problem Statement

Managing personal and shared finances can be challenging, especially for couples who need to keep track of joint income and expenses. <br>
Many existing financial management tools offer comprehensive budget planning features, but they often fall short in providing a simple and efficient way to track financial transactions among multiple users. <br>
This can lead to difficulties in maintaining shared finances, resulting in misunderstandings or conflicts over financial matters.

Personally, I've tried budgeting apps, but nothing suited what I needed, leaving my wife and me to compare expenses at the end of the week. This left holes in our budget. <br>
I've spent many hours on the internet in search of an expense tracker that can be shared between couples so that no expense is left untracked. <br><br>

I haven't yet found one that works for me... next best solution? create my own.

### Solution

The Income and Expense Tracker API is here to make managing money easier for couples. <br>
It simplifies how you track your finances, allowing you to effortlessly record income and expenses. <br>
It provides a user-friendly solution for tracking financial transactions, focusing on recording income and expenses while supporting the sharing of transaction accounts between partners. <br>

Here’s how the app will address the problem:

#### Simplified Financial Tracking

The API makes it easy to record income and expenses, capturing key details like transaction type, amount, date, and description. This straightforward approach helps couples keep accurate financial records without the hassle of a complex budget planner.

#### Shared Accounts

A standout feature is the ability to share transaction accounts with multiple users, perfect for couples managing joint finances. Both partners can view and record transactions, encouraging transparency and collaboration.

#### User Roles and Permissions

The API allows for assigning different roles within shared accounts, such as owner, user, or authorised user. This role-based access control ensures each partner has the right level of access and permissions, ensuring security.

#### Categorisation & Organisation

Users can categorise transactions to better organise their financial data. This helps couples understand their spending patterns and income sources, making financial planning and decision-making easier.

#### Real-time Collaboration

With multiple users able to interact with the same account in real-time, the API ensures all financial data is up-to-date and accessible to both partners. This eliminates delays and ensures everyone is on the same page about their financial status.

The Income and Expense Tracker API addresses the common challenges couples face in managing their joint finances. By focusing on simplicity, shared account functionality, user roles, categorisation, and real-time collaboration, the API provides a solution for financial organisation, and cooperation. This approach makes it easier for couples to manage their income and expenses, reducing the financial misunderstandings.

## R2: Task Allocation and Tracking

To ensure thorough task management and progress tracking, I use Trello. <br>
Trello allows me to organise tasks visually and track their status through various stages of completion.

1. <b>Task Allocation</b>

   - <b>Task Creation:</b> I create tasks as individual Trello cards, each representing a specific task that needs completion.
   - <b>Details and Deadlines:</b> Each card includes a detailed description, relevant attachments and checklists. This keeps me organised and ensures I have all necessary information to complete the task.

2. <b>Tracking Progress</b>

   - <b>Backlog:</b> This list contains all tasks that need to be done eventually but are not yet prioritised. It's future tasks that I can move to "To Do" when ready to start working on them.

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


## R6: ERD Design

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

- `category_id` (Integer)
- `category_name` (String: max length 100, not nullable)
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
