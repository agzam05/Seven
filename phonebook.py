import psycopg2
import csv
conn=psycopg2.connect(
    host="localhost",
    database="postgres",
    user="abilshahmatagzam",
    password="8990"
)
cur=conn.cursor()
cur.execute(
    "DELETE FROM phonebook"
)
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20)
            )
""")
firstname=input("Name you want to insert")
phone=input("Phone you want to insert")
cur.execute("" \
"INSERT INTO phonebook (first_name, phone) VALUES(%s, %s)", (firstname, phone))
with open("/Users/abilshahmatagzam/Desktop/pg_project/contacts.csv", "r") as file:
    file_reader=csv.reader(file)
    next(file_reader)
    for row in file_reader:
        first_name=row[0]
        phone=row[1]
        cur.execute("INSERT INTO phonebook (first_name,phone) VALUES (%s, %s)",(first_name, phone))
updatename=input("Enter the name you want to update")
updatephone=input("Enter the phone you want to update")
cur.execute(
    "UPDATE phonebook SET phone=%s WHERE first_name=%s", (updatephone, updatename)
)
conn.commit()
find=input("Enter the name  you want to find")
cur.execute("SELECT * FROM phonebook WHERE first_name=%s", (find,))
rows=cur.fetchall()
if len(rows)!=0:
    print("Your name succesfully find Here you go")
    for row in rows:
        print(row)
else:
    print("Not Found")
delete=input("For deleting by name write (1), else (2)")
if delete=='1':
    name=input("Enter the name for deleting")
    cur.execute(
        "DELETE FROM phonebook WHERE first_name=%s", (name,)
    )
else:
    pho=input("Enter the phone you want to delete ")
    cur.execute(
        "DELETE FROM phonebook WHERE phone=%s", (pho,)
    )

cur.execute(
    "SELECT * FROM phonebook"
)
rows=cur.fetchall()
for row in rows:
    print(row)
conn.commit()
cur.close()
conn.close()