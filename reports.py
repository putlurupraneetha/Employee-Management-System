from db_connection import get_connection


# ===== Attendance Report =====
def generate_attendance_report(emp_id=None):
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


# ===== Leave Report =====
def generate_leave_report(emp_id=None):
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


# ===== Combined Attendance + Leave Report =====
def generate_combined_report(emp_id=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            e.EmpID, e.Name, a.Date AS AttendanceDate, a.Status AS AttendanceStatus,
            l.StartDate AS LeaveStart, l.EndDate AS LeaveEnd, l.Reason AS LeaveReason, l.Status AS LeaveStatus
        FROM Employee e
        LEFT JOIN Attendance a ON e.EmpID = a.EmpID
        LEFT JOIN LeaveRequests l ON e.EmpID = l.EmpID
        """
        if emp_id:
            query += " WHERE e.EmpID = ?"
            cursor.execute(query, (emp_id,))
        else:
            cursor.execute(query)

        rows = cursor.fetchall()

        if rows:
            print(
                "\nEmpID | Name       | AttendanceDate | AttendanceStatus | LeaveStart | LeaveEnd | LeaveReason | LeaveStatus")
            print("-" * 120)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]}")
        else:
            print("No combined records found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
