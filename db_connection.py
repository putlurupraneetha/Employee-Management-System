import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=Praneetha\\SQLEXPRESS;'
        'DATABASE=EMS;'
        'Trusted_Connection=yes;'
        'Encrypt=no;'
    )
    return conn
