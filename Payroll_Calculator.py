# Hint: Company has a fixed roster of employees each pay period
employees = 12
total_payroll = 0

for i in range(employees):
    print(f"Employee {i+1}")
    employee_num = float(input("Enter  number employees : ")) # Employee number
    hours_worked = float(input("Enter number of hours worked: ")) # Hours worked
    overtime_hours = float(input("Enter number of overtime hours worked: ")) # Overtime hours worked
    hourly_pay = float(input("Enter hourly pay rate: ")) # Hourly pay rate
if hours_worked > 40:
    print("THE MAX IS 40")
    
    regular_pay = hours_worked * hourly_pay # Regular pay
    overtime_pay = overtime_hours * hourly_pay * 1.5 # Overtime pay
    total_pay = regular_pay + overtime_pay # Total pay

    print(f"{employee_num}'s total pay: ${total_pay:.2f}") # Display total pay
    total_payroll += total_pay



# Think: How do you process a predetermined number of employees?
# Your processing structure here 
