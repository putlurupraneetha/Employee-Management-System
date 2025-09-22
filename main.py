from employee import add_employee, view_employees
from attendance import mark_attendance, view_attendance, update_attendance, delete_attendance
from leave import apply_leave, view_leave, update_leave, delete_leave
from reports import generate_attendance_report, generate_leave_report, generate_combined_report
from datetime import datetime

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Employee Management")
        print("2. Attendance Management")
        print("3. Leave Management")
        print("4. Reports")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            employee_menu()
        elif choice == '2':
            attendance_menu()
        elif choice == '3':
            leave_menu()
        elif choice == '4':
            reports_menu()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# ===== Employee Menu =====
def employee_menu():
    while True:
        print("\n--- Employee Menu ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Back")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            dept = input("Enter department: ").strip()
            designation = input("Enter designation: ").strip()
            joining_date = input("Enter joining date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(joining_date, "%Y-%m-%d")
                add_employee(name, dept, designation, joining_date)
            except ValueError:
                print("Invalid date format! Use YYYY-MM-DD.")
        elif choice == '2':
            view_employees()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# ===== Attendance Menu =====
def attendance_menu():
    while True:
        print("\n--- Attendance Menu ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Update Attendance")
        print("4. Delete Attendance")
        print("5. Back")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                emp_id = int(input("Enter Employee ID: "))
                status = input("Enter status (Present/Absent/Leave): ").capitalize()
                att_date = input("Enter date (YYYY-MM-DD, leave blank for today): ").strip()
                att_date = att_date if att_date else None
                mark_attendance(emp_id, status, att_date)
            except ValueError:
                print("Invalid input!")
        elif choice == '2':
            emp_id_input = input("Enter Employee ID (leave blank for all): ").strip()
            emp_id = int(emp_id_input) if emp_id_input else None
            view_attendance(emp_id)
        elif choice == '3':
            att_id = int(input("Enter AttendanceID to update: "))
            status = input("Enter new status (Present/Absent/Leave): ").capitalize()
            update_attendance(att_id, status)
        elif choice == '4':
            att_id = int(input("Enter AttendanceID to delete: "))
            delete_attendance(att_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# ===== Leave Menu =====
def leave_menu():
    while True:
        print("\n--- Leave Menu ---")
        print("1. Apply Leave")
        print("2. View Leave")
        print("3. Update Leave Status")
        print("4. Delete Leave")
        print("5. Back")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                emp_id = int(input("Enter Employee ID: "))
                start_date = input("Enter start date (YYYY-MM-DD): ").strip()
                end_date = input("Enter end date (YYYY-MM-DD): ").strip()
                reason = input("Enter reason: ").strip()
                apply_leave(emp_id, start_date, end_date, reason)
            except ValueError:
                print("Invalid input!")
        elif choice == '2':
            emp_id_input = input("Enter Employee ID (leave blank for all): ").strip()
            emp_id = int(emp_id_input) if emp_id_input else None
            view_leave(emp_id)
        elif choice == '3':
            leave_id = int(input("Enter LeaveID to update: "))
            status = input("Enter new status (Pending/Approved/Rejected): ").capitalize()
            update_leave(leave_id, status)
        elif choice == '4':
            leave_id = int(input("Enter LeaveID to delete: "))
            delete_leave(leave_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# ===== Reports Menu =====
def reports_menu():
    while True:
        print("\n--- Reports Menu ---")
        print("1. Attendance Report")
        print("2. Leave Report")
        print("3. Combined Attendance + Leave Report")
        print("4. Back")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            emp_id_input = input("Enter Employee ID (leave blank for all): ").strip()
            emp_id = int(emp_id_input) if emp_id_input else None
            generate_attendance_report(emp_id)
        elif choice == '2':
            emp_id_input = input("Enter Employee ID (leave blank for all): ").strip()
            emp_id = int(emp_id_input) if emp_id_input else None
            generate_leave_report(emp_id)
        elif choice == '3':
            emp_id_input = input("Enter Employee ID (leave blank for all): ").strip()
            emp_id = int(emp_id_input) if emp_id_input else None
            generate_combined_report(emp_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

# ===== Run the program =====
if __name__ == "__main__":
    main_menu()
