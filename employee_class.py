#  CS 3B Intermediate Software Design in Python
#  Lab # 3
#  Module: Inheritance
#  Description: This programs design a base class of Employee, that will
#               be extended to two subclasses: ProductionWorker and
#               ShiftSuperVisor. These classes will contain employee
#               information for a certain company.
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantoa3.py
#  Date:  2/23/23
#

# Import Classes
from decimal import *


# Base Class
class Employee:
    # Constants
    DEFAULT_EMPNAME = None
    DEFAULT_EMPNUM = None
    DATATYPE_EMPNAME = str
    DATATYPE_EMPNUM = int
    MAX_LENGTH_EMPNAME = 20
    MAX_LENGTH_EMPNUM = 8
    """
    Constructs an employee object with a given Employee name and number
    @param emp_name - the name of the employee
    @param emp_num - the employee number of the employee
    """
    def __init__(self, emp_name, emp_num):
        self._empName = Employee.DEFAULT_EMPNAME
        self._empNum = Employee.DEFAULT_EMPNUM
        self.setEmpName(emp_name)
        self.setEmpNum(emp_num)

    """
    Changes the name of the employee
    @param emp_name - the name of the employee
    @return success - bool if set operation is successful
    """
    def setEmpName(self, emp_name):
        if (isinstance(emp_name, Employee.DATATYPE_EMPNAME)) and (len(
                emp_name) <= Employee.MAX_LENGTH_EMPNAME):
            self._empName = emp_name
            return True
        else:
            self._empName = Employee.DEFAULT_EMPNAME
            return False

    """
    Changes the employee number of the employee
    @param emp_num - the employee number of the employee
    @return success - bool if set operation is successful
    """
    def setEmpNum(self, emp_num):
        if (isinstance(emp_num, Employee.DATATYPE_EMPNUM)) and (len(str(
                emp_num)) == Employee.MAX_LENGTH_EMPNUM):
            self._empNum = emp_num
            return True
        else:
            self._empNum = Employee.DEFAULT_EMPNUM
            return False

    """
    Gets the name of the employee
    @return emp_name - the name of the employee
    """
    def getEmpName(self):
        return self._empName

    """
    Gets the employee number of the employee
    @return emp_num - the employee number of the employee
    """
    def getEmpNum(self):
        return self._empNum

    """
    Gets overall description of the employee
    """
    def getDescription(self):
        print("Employee Name: " + self.getEmpName())
        print("Employee ID: " + str(self.getEmpNum()))


# Subclasses
class ProductionWorker(Employee):
    """
    Constructs a ProductionWorker object that contains empName, empNum,
    shiftNum and hourlyPayRate
    """
    # Constants
    DEFAULT_SHIFTNUM = None
    DEFAULT_HOURLYPR = None
    DATATYPE_SHIFTNUM = int
    DATATYPE_HOURLYPR = (int, float)
    OPTION_SHIFTNUM = (1, 2)
    MIN_HOURLYPR = 0

    def __init__(self):
        self._empName = Employee.DEFAULT_EMPNAME
        self._empNum = Employee.DEFAULT_EMPNUM
        self._shiftNum = ProductionWorker.DEFAULT_SHIFTNUM
        self._hourlyPayRate = ProductionWorker.DEFAULT_HOURLYPR

    """
    Changes the shiftNumber of the production worker
    @param shift_num - the shift number of the production worker (1 for day 
                        shift, 2 for night shift)
    @return success - bool if set operation is successful
    """
    def setShiftNum(self, shift_num):
        if isinstance(shift_num, ProductionWorker.DATATYPE_SHIFTNUM) and (
                shift_num in ProductionWorker.OPTION_SHIFTNUM):
            self._shiftNum = shift_num
            return True
        else:
            self._shiftNum = ProductionWorker.DEFAULT_SHIFTNUM
            return False

    """
    Changes the hourlyPayRate of the production worker
    @param hourly_pay - the hourly pay rate of the production worker. 
                        Cannot be negative.
    @return success - bool if set operation is successful
    """
    def setHourlyPayRate(self, hourly_pay):
        if isinstance(hourly_pay, ProductionWorker.DATATYPE_HOURLYPR) and \
                hourly_pay >= ProductionWorker.MIN_HOURLYPR:
            self._hourlyPayRate = Decimal(hourly_pay)
            return True
        else:
            self._hourlyPayRate = ProductionWorker.DEFAULT_HOURLYPR
            return False

    """
    Gets the shift number of the production worker
    @return shift_num - the shift number of the production worker   
    """
    def getShiftNum(self):
        return self._shiftNum

    """
    Gets the hourly pay rate of the production worker
    @return hourly_pay - the hourly pay rate of teh production worker
    """
    def getHourlyPayRate(self):
        return self._hourlyPayRate

    """
    Gets the hourly pay rate of the production worker in currency format
    @return salary - the hourly pay rate of the production worker in currency 
                     format
    """
    def getHourlyPayRateCurrency(self):
        return "$" + "{:,.2f}".format(self.getHourlyPayRate())

    """
    Gets overall description of the production worker
    """
    def getDescription(self):
        print("Employee Name: " + self.getEmpName())
        print("Employee ID: " + str(self.getEmpNum()))
        print("Shift Number: " + str(self.getShiftNum()))
        print("Hourly Pay Rate: " + self.getHourlyPayRateCurrency())


class ShiftSuperVisor(Employee):
    # Constants
    DEFAULT_SALARY = None
    DEFAULT_BONUS = None
    DATATYPE_SALARY = (int, float)
    DATATYPE_BONUS = (int, float)
    MIN_SALARY = 0
    MIN_BONUS = 0

    """
    Constructs a ShiftSuperVisor object that contains empName, empNum,
    salary and bonus.
    """
    def __init__(self):
        self._empName = Employee.DEFAULT_EMPNAME
        self._empNum = Employee.DEFAULT_EMPNUM
        self._salary = ShiftSuperVisor.DEFAULT_SALARY
        self._bonus = ShiftSuperVisor.DEFAULT_BONUS

    """
    Changes the salary of the shift supervisor
    @param salary - the salary of the supervisor
    @return success - bool if set operation is successful
    """
    def setSalary(self, salary):
        if isinstance(salary, ShiftSuperVisor.DATATYPE_SALARY) and salary >=\
                ShiftSuperVisor.MIN_SALARY:
            self._salary = Decimal(salary)
            return True
        else:
            self._salary = ShiftSuperVisor.DEFAULT_SALARY
            return False

    """
    Changes the bonus of the shift supervisor
    @param bonus - the yearly bonus of the supervisor
    @return success - bool if set operation is successful
    """
    def setBonus(self, bonus):
        if isinstance(bonus, ShiftSuperVisor.DATATYPE_BONUS) and bonus >= \
                ShiftSuperVisor.MIN_BONUS:
            self._bonus = Decimal(bonus)
            return True
        else:
            self._bonus = ShiftSuperVisor.DEFAULT_BONUS
            return False

    """
    Gets the salary of the shift supervisor
    @return salary - the salary of the shift supervisor
    """
    def getSalary(self):
        return self._salary

    """
    Gets the salary of the shift supervisor in currency format
    @return salary - the salary of the shift supervisor in currency format
    """
    def getSalaryCurrency(self):
        return "$" + "{:,.2f}".format(self.getSalary())

    """
    Gets the bonus of the shift supervisor
    @return bonus - the yearly bonus of the shift supervisor
    """
    def getBonus(self):
        return self._bonus

    """
    Gets the bonus of the shift supervisor in currency format
    @return bonus - the yearly bonus of the shift supervisor in currency format
    """
    def getBonusCurrency(self):
        return "$" + "{:,.2f}".format(self.getBonus())

    """
    Gets overall description of the shift supervisor
    """
    def getDescription(self):
        print("Employee Name: " + self.getEmpName())
        print("Employee ID: " + str(self.getEmpNum()))
        print("Salary: " + self.getSalaryCurrency())
        print("Bonus: " + self.getBonusCurrency())
