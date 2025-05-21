import mysql.connector

def get_connections():
    return mysql.connector.connect(
    host = "localhost",
    username= "root",
    password = "root254",
    database = "Expense_tracker"
    
    )
    
