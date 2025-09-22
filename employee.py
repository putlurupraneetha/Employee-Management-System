from db_connection import get_connection

# ===== Create =====
def add_employee(name, dept, designation, joining_date):
    """
    Add a new employee.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Employee (Name, Dept, Designation, JoiningDate)
            VALUES (?, ?, ?, ?)
        """, (name, dept, designation, joining_date))
        conn.commit()
        print("Employee added successfully!")
    except Exception as e:
        print("Error adding employee:", e)
    finally:
        conn.close()


# ===== Read =====
def view_employees():
    """
    View all employees.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        rows = cursor.fetchall()
        if rows:
            print("\nEmpID | Name | Dept | Designation | JoiningDate")
            print("-"*50)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        else:
            print("No employees found.")
    except Exception as e:
        print("Error viewing employees:", e)
    finally:
        conn.close()


# ===== Update =====
def update_employee(emp_id, name=None, dept=None, designation=None, joining_date=None):
    """
    Update employee details. Only provided fields will be updated.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Build dynamic query based on provided fields
        fields = []
        values = []

        if name:
            fields.append("Name = ?")
            values.append(name)
        if dept:
            fields.append("Dept = ?")
            values.append(dept)
        if designation:
            fields.append("Designation = ?")
            values.append(designation)
        if joining_date:
            fields.append("JoiningDate = ?")
            values.append(joining_date)

        if not fields:
            print("No fields to update.")
            return

        values.append(emp_id)
        query = f"UPDATE Employee SET {', '.join(fields)} WHERE EmpID = ?"
        cursor.execute(query, values)
        conn.commit()
        print("Employee updated successfully!")
    except Exception as e:
        print("Error updating employee:", e)
    finally:
        conn.close()


# ===== Delete =====
def delete_employee(emp_id):
    """
    Delete an employee by ID.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Employee WHERE EmpID = ?", (emp_id,))
        conn.commit()
        print("Employee deleted successfully!")
    except Exception as e:
        print("Error deleting employee:", e)
    finally:
        conn.close()
