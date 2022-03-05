import sqlite3

con = sqlite3.connect("pics/photo_frame.db")

cur = con.cursor()

# Create table
cur.execute(
    """CREATE TABLE images
               (path text, fname text, date text)"""
)

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
