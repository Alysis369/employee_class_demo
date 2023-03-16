#  CS 3B Intermediate Software Design in Python
#  Lab # 3
#  Module: Inheritance
#  Description: This programs design a base class of Employee, that will
#               be extended to two subclasses: ProductionWorker and
#               ShiftSuperVisor. These classes will contain employee
#               information for a certain company.
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantotest3.py
#  Date:  2/23/23
#

# Class Import
from aldosiswantoa3 import Employee, ProductionWorker, ShiftSuperVisor


def main():
    # Create demo production worker object
    print("Demo production worker")
    prod_worker_obj = ProductionWorker()

    # Input production worker details
    emp_name_input = input("Enter the name: ")
    if not (prod_worker_obj.setEmpName(emp_name_input)):
        print("Invalid employee name input. Max 20 letters.")

    emp_num_input = int(input("Enter the ID number: "))
    if not (prod_worker_obj.setEmpNum(emp_num_input)):
        print("Invalid employee number input. 8 digit number.")

    shift_num_input = int(input("Enter the shift number: "))
    if not (prod_worker_obj.setShiftNum(shift_num_input)):
        print("Invalid shift number input. 1 or 2.")

    hourly_pay_rate_input = float(input("Enter the hourly pay rate: "))
    if not (prod_worker_obj.setHourlyPayRate(hourly_pay_rate_input)):
        print("Invalid hourly pay rate input. Int/Float, more than 0")

    # Display production worker details
    print("\nProduction worker information:")
    prod_worker_obj.getDescription()

    # Create demo shift supervisor object
    print("\nDemo shift supervisor worker")
    shift_supervisor_obj = ShiftSuperVisor()

    # Input shift supervisor details
    emp_name_input = input("Enter the name: ")
    if not (shift_supervisor_obj.setEmpName(emp_name_input)):
        print("Invalid employee name input. Max 20 letters.")

    emp_num_input = int(input("Enter the ID number: "))
    if not (shift_supervisor_obj.setEmpNum(emp_num_input)):
        print("Invalid employee number input. 8 digit number.")

    salary_input = float(input("Enter the Annual Salary: "))
    if not (shift_supervisor_obj.setSalary(salary_input)):
        print("Invalid annual salary input. Int/Float, more than 0")

    bonus_input = float(input("Enter the Annual Bonus: "))
    if not (shift_supervisor_obj.setBonus(bonus_input)):
        print("Invalid annual bonus input. Int/Float, more than 0")

    # Display production worker details
    print("\nShift supervisor worker information:")
    shift_supervisor_obj.getDescription()


if __name__ == "__main__":
    main()

"""
Demo production worker
Enter the name: Ann Foothill
Enter the ID number: 12345678
Enter the shift number: 2
Enter the hourly pay rate: 16.75

Production worker information:
Employee Name: Ann Foothill
Employee ID: 12345678
Shift Number: 2
Hourly Pay Rate: $16.75

Demo shift supervisor worker
Enter the name: Bob De Anza
Enter the ID number: 87654321
Enter the Annual Salary: 100000
Enter the Annual Bonus: 12000

Shift supervisor worker information:
Employee Name: Bob De Anza
Employee ID: 87654321
Salary: $100,000.00
Bonus: $12,000.00

"""