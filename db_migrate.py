import sys
sys.path.append('..')

from views import db
from _config import DATABASE

import sqlite3
from datetime import datetime

with sqlite3.connect(str(DATABASE)) as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # # temporarily change the name of tasks table
    # c.execute("""ALTER TABLE users RENAME TO old_users""")

    # recreate a new tasks table with updated schema
    db.create_all()

    # retrieve data from old_tasks table
    c.execute("""SELECT name, email, password
    FROM old_users ORDER BY id ASC""")

    # save all rows as a list of tuples; set role to user
    data = [(row[0], row[1], row[2], 'user') for row in c.fetchall()]

    # insert data to tasks table
    c.executemany("""INSERT INTO users (name, email, password, role)
    VALUES (?, ?, ?, ?)""", data)

    # # delete old_tasks table
    # c.execute("DROP TABLE old_tasks")