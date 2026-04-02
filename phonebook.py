import psycopg2
import csv
conn=psycopg2.connect(
    host="localhost",
    database="postgres",
    user="abilshahmatagzam",
    password="8990"
)
cur=conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20)
            )
""")
firstname=input("Enter the name you want to add")
phone=input("Enter phone number you want to add")
cur.execute(
    "INSERT INTO phonebook (first_name, phone) VALUES(%s, %s)", (firstname, phone) 
)
with open("contacts.csv", "r") as file:
    file_reader=csv.reader(file)
    next(file_reader)
    for row in file_reader:
        firtname=row[0]
        phne=row[1]
        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (firtname, phne)
        )
choice=input("If you want to change number enter (1), else (2)")
if choice=='1':
    updaten=input("Enter name whose number you want to change")
    updatep=input("Enter updated phone")
    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE first_name=%s", (updatep, updaten)
    )
else:
    update=input("Enter person's number you want to rename")
    updatename=input("Enter updated name ")
    cur.execute(
        "UPDATE phonebook SET first_name=%s WHERE phone=%s", (updatename, update)
    )
conn.commit()
n=input("How you want to find by name (1), else (2)")
if n=='1':
    find=input("Enter who you want to find")
    cur.execute(
    "SELECT * FROM phonebook WHERE first_name=%s", (find,)
)
    rows=cur.fetchall()
    if len(rows)!=0:
        for row in rows:
            print(row)
            print("succesfully finded")
    else:
        print("Not Found")

elif n=='2':
    finding=input("Enter the number you want to find")
    cur.execute(
        "SELECT * FROM phonebook WHERE phone=%s", (finding,)
    )
    row=cur.fetchall()
    if len(row)!=0:
        for ro in row:
         print(ro)
         print("Finded succesfully")
    else:
        print("Not Found")
d=input("How do you want to delete by name(1), by number(2) ")
if d=='1':
    deletename=input("Enter the name you want to delete")
    if len(deletename)!=0:
        cur.execute(
            "DELETE FROM phonebook WHERE first_name=%s", (deletename,)
        )
        print("Deleted Succesfully ")
        conn.commit()
    else:
        print("This name not Found")
else:
    deletenumber=input("Enter the phone you want to delete")
    if len(deletenumber)!=0:
        cur.execute(
            "DELETE FROM phonebook WHERE phone=%s", (deletenumber,)
        )
        conn.commit()
        print("Deleted Succesfully ")
    else:
        print("Not Found")
cur.execute(
    "SELECT * FROM phonebook"
)
rows=cur.fetchall()
for row in rows:
    print(row)
conn.commit()
cur.close()
conn.close()