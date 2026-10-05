# Review Programming Assignment
# Program Description: Employee Directory Program
# Your Name: Lincoln
# Date: 2026-10-04


# Employee Class
class Employee:
    """ Employee class to keep track employee info """

    def __init__(self, ID=-999, name='', department='', pay=0.0):
        """ initializer for new employee object """
        self.set_ID(ID)
        self.set_name(name)
        self.set_department(department)
        self.set_pay(pay)

    def get_ID(self):
        """ return employee id """
        return self.ID

    def set_ID(self, ID):
        """ assign employee id """
        self.ID = ID

    def get_name(self):
        """ return employee name """
        return self.name

    def set_name(self, name):
        """ assign employee name """
        self.name = name

    def get_department(self):
        """ return employee department """
        return self.department

    def set_department(self, department):
        """ assign employee department """
        self.department = department

    def get_pay(self):
        """ return employee pay """
        return self.pay

    def set_pay(self, pay):
        """ assign employee pay """
        self.pay = pay

    def __str__(self):
        """ return employee object in string """
        return f'{self.get_ID()}\t{self.get_name()}\t{self.get_department()}\t{self.get_pay()}'

    def __eq__(self, other):
        """ compare employees by ID """
        return isinstance(other, Employee) and self.get_ID() == other.get_ID()


class EmployeeDirectory:
    """ Track employee info in the directory """

    def __init__(self):
        """ initialize employee_list and employee_dict """
        self.employee_list = []
        self.employee_dict = {}

    def add_employee(self, employee):
        """ append employee object to the employee_list """
        if employee in self.employee_list:
            return
        self.employee_list.append(employee)

    def del_employee(self, employee):
        """ delete employee object from the employee_list """
        if employee not in self.employee_list:
            print(f"ID:{employee.get_ID()} does not exist, deletion is aborted")
            return
        self.employee_list.remove(employee)

    def read_file(self, file_name):
        """ read employees.txt file and store the data into a list of employee objects and return it """
        employee_list = []
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) >= 4:
                    employee = Employee(int(parts[0]), parts[1], parts[2], float(parts[3]))
                    employee_list.append(employee)
        return employee_list

    def update_employee_dir(self, file_name):
        """ call read_file and update the employee_list attribute """
        self.employee_list = self.read_file(file_name)

    def write_to_file(self, file_name):
        """ write the updated employee_list to file """
        with open(file_name, 'w') as file:
            for employee in self.employee_list:
                file.write(f"{employee.get_ID()} {employee.get_name()} {employee.get_department()} {employee.get_pay()}\n")

    def write_to_dict(self):
        """ write employee_list data to a dictionary of lists, update the employee_dict attribute """
        self.employee_dict = {'ID': [], 'name': [], 'department': [], 'pay': []}
        for emp in self.employee_list:
            self.employee_dict['ID'].append(emp.get_ID())
            self.employee_dict['name'].append(emp.get_name())
            self.employee_dict['department'].append(emp.get_department())
            self.employee_dict['pay'].append(emp.get_pay())

    def display_dict(self):
        """ display employee dictionary in key/value pairs """
        print(f"ID        : {self.employee_dict['ID']}")
        print(f"name      : {self.employee_dict['name']}")
        print(f"department: {self.employee_dict['department']}")
        print(f"pay       : {self.employee_dict['pay']}")


# test class
if __name__ == '__main__':

    try:
        # Create an object of EmployeeDirectory
        directory = EmployeeDirectory()

        # Call update_employee_dir() method
        directory.update_employee_dir('employees.txt')

        # Add 3 employee objects as specified in the assignment
        emp1 = Employee(106, 'Emp1', 'Accounting', 56000.0)
        emp2 = Employee(107, 'Emp2', 'Sales', 80000.0)
        emp3 = Employee(108, 'Emp3', 'Marketing', 90000.0)

        # Add emp1 and emp2 objects to the directory
        directory.add_employee(emp1)
        directory.add_employee(emp2)

        # Delete emp3, which is not in the directory yet, to match the sample output
        directory.del_employee(emp3)

        # Overwrite the employee file with the updated list
        directory.write_to_file('employees.txt')

        # Convert the list to a dictionary and display it
        directory.write_to_dict()
        directory.display_dict()

    except FileNotFoundError as fnfe:
        print(fnfe)
    except KeyError as ke:
        print(ke)
    except Exception as ex:
        print(ex)


