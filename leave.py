from db_connection import get_connection

# ===== Create / Apply Leave =====
def apply_leave(emp_id, start_date, end_date, reason):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO LeaveRequests (EmpID, StartDate, EndDate, Reason, Status)
            VALUES (?, ?, ?, ?, ?)
        """, (emp_id, start_date, end_date, reason, "Pending"))
        conn.commit()
        print("Leave applied successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# ===== Read / View Leave =====
def view_leave(emp_id=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if emp_id:
            cursor.execute("SELECT * FROM LeaveRequests WHERE EmpID = ?", (emp_id,))
        else:
            cursor.execute("SELECT * FROM LeaveRequests")
        rows = cursor.fetchall()
        if rows:
            print("\nLeaveID | EmpID | StartDate  | EndDate    | Reason       | Status")
            print("-" * 80)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
        else:
            print("No leave records found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# ===== Update Leave =====
def update_leave(leave_id, status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE LeaveRequests
            SET Status = ?
            WHERE LeaveID = ?
        """, (status, leave_id))
        conn.commit()
        if cursor.rowcount:
            print("Leave status updated successfully!")
        else:
            print("Leave ID not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# ===== Delete Leave =====
def delete_leave(leave_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM LeaveRequests WHERE LeaveID = ?", (leave_id,))
        conn.commit()
        if cursor.rowcount:
            print("Leave deleted successfully!")
        else:
            print("Leave ID not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
