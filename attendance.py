from db_connection import get_connection
from datetime import date

# ===== Create / Mark Attendance =====
def mark_attendance(emp_id, status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        today = date.today()
        cursor.execute("""
            INSERT INTO Attendance (EmpID, Date, Status)
            VALUES (?, ?, ?)
        """, (emp_id, today, status))
        conn.commit()
        print("Attendance marked successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# ===== Read / View Attendance =====
def view_attendance(emp_id=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if emp_id:
            cursor.execute("SELECT * FROM Attendance WHERE EmpID = ?", (emp_id,))
        else:
            cursor.execute("SELECT * FROM Attendance")
        rows = cursor.fetchall()
        if rows:
            print("\nAttendanceID | EmpID | Date       | Status")
            print("-" * 45)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        else:
            print("No attendance records found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# ===== Update Attendance =====
def update_attendance(attendance_id, status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Attendance
            SET Status = ?
            WHERE AttendanceID = ?
        """, (status, attendance_id))
        conn.commit()
        if cursor.rowcount:
            print("Attendance updated successfully!")
        else:
            print("Attendance ID not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# ===== Delete Attendance =====
def delete_attendance(attendance_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Attendance WHERE AttendanceID = ?", (attendance_id,))
        conn.commit()
        if cursor.rowcount:
            print("Attendance deleted successfully!")
        else:
            print("Attendance ID not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
