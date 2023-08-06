

import sqlite3

# conn = sqlite3.connect("customer.db") (creates temporary database in memory)

# connect to a database named customer.db
conn = sqlite3.connect("customer.db")

# create a cursor
c = conn.cursor()

# # create a table
# c.execute(""" CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
#     )""")
#
# # DATATYPES:
# # Null
# # Integer
# # Real
# # Text
# # Blob


# Table is created, now we need to insert data into table
# Single data insertion
# c.execute("INSERT INTO customers VALUES ('Pathrose', 'Dsouza', 'p.dsouza@mail.com')")

# Multiple data insertion
# many_customers = [
#                     ('Ram', 'Choudhary','r.chau@gmail.com'),
#                     ('Shyam', 'Shrestha','s.sh@gmail.com'),
#                     ('Krishna', 'Choudhary','k.chau@gmail.com')
#                 ]
#
# c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)


# UPDATING CUSTOMERS
c.execute("""UPDATE customers SET first_name = 'Yugendra'
            WHERE last_name = 'Ray'
""" )
conn.commit()


# Query the database
c.execute("SELECT rowid, * FROM customers")
# WHERE is used to search specific data
#c.fetchone()
#c.fetchmany(3)

items = c.fetchall()
# print(items)

for item in items:
   print(item)

# print("NAME" + "\t\t\t\t\tEMAIL")
# print("--------" +"\t\t\t\t"+  "----------")
#
# for item in items:
#     print(item[0] + " " + item[1] + "\t\t\t\t" + item[2])



# Commit our command
conn.commit()

# Close our connection
conn.close()
