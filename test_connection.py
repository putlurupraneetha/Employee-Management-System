from db_connection import get_connection

try:
    conn = get_connection()
    print("Connected Successfully!")
except Exception as e:
    print("Connection failed!")
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()
