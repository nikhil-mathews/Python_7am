import sqlite3

database="mytodo.db"
table="tasks"

con = sqlite3.connect(database)
cur = con.cursor()

def create_table():
    cur.execute('''CREATE TABLE  IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT , taskname TEXT)''')
    print("table created successfully!!")

def add_task(task):
    cur.execute("INSERT INTO tasks (taskname) VALUES (?)",[task])
    print("Task added successfully!!")
    con.commit()

def display_task():
    cur.execute("select * from tasks")
    for row in cur.fetchall():
        print(f"{row[0]} --> {row[1]}")

def delete_task(ind):
    cur.execute("DELETE from tasks where id=(?)",[ind,])
    print("Deleted successfully")

def update_task(id,updated_task):
    cur.execute("Update tasks set taskname=(?) where id =(?)",[updated_task,id])
    con.commit()
    print("Updated successfully!!")

def close_connection():
    cur.close()
    con.close()