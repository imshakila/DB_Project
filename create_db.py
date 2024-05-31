import mysql.connector

def create_database(cursor, database_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f" {database_name} created successfully.")

def show_databases(cursor):
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print("Databases:", databases)
    return databases

def create_table(cursor, table_query):
    cursor.execute(table_query)
    print("Table created successfully.")

def connect_to_db(host, user, password, database=None):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
def create_db(db_name):
    mydb = connect_to_db("localhost", "root", "pass")
    cursor = mydb.cursor()
