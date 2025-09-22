from reports import generate_attendance_report, generate_leave_report

# Test attendance report for all employees
generate_attendance_report()

# Test leave report for all employees
generate_leave_report()

# Test reports for a specific employee (EmpID = 1)
generate_attendance_report(emp_id=1)
generate_leave_report(emp_id=1)
