"""importing necessary modules json for working with JSON data, Faker for generating fake data"""
import json
from faker import Faker
from PythonAssignmentW2.ques1 import log_execution_time

class Employee:
    """
    Represents an employee and provides methods to convert 
    employee data to JSON format and write it to files.
    """
    @log_execution_time
    def __init__(self, emp_id=None, emp_name=None, emp_email=None, business_unit=None, salary=None):
        """
        Initializes an Employee object with the provided values for the attributes
        """
        self._faker = Faker()
        self.emp_id = emp_id if emp_id is not None else self._faker.random_int(min=1000, max=9999)
        self.emp_name = emp_name if emp_name else self._faker.name()
        self.emp_email = emp_email if emp_email else self._faker.email()
        self.business_unit = business_unit if business_unit else self._faker.company()
        self.salary =salary if salary is not None else self._faker.random_int(min=30000, max=100000)

    @property
    def emp_id(self):
        """Getter and setter method for the emp_id attribute."""
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value

    @property
    def emp_name(self):
        """Getter and setter method for the emp_name attribute."""
        return self._emp_name

    @emp_name.setter
    def emp_name(self, value):
        self._emp_name = value

    @property
    def emp_email(self):
        """Getter and setter method for the emp_email attribute."""
        return self._emp_email

    @emp_email.setter
    def emp_email(self, value):
        self._emp_email = value

    @property
    def business_unit(self):
        """Getter and setter method for the business_unit attribute."""
        return self._business_unit

    @business_unit.setter
    def business_unit(self, value):
        self._business_unit = value

    @property
    def salary(self):
        """Getter and setter method for the salary attribute."""
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @log_execution_time
    def to_json(self):
        """Converts the Employee object to a JSON-formatted dictionary."""
        return {
            "emp_id": self.emp_id,
            "emp_name": self.emp_name,
            "emp_email": self.emp_email,
            "business_unit": self.business_unit,
            "salary": self.salary
        }

    @log_execution_time
    def to_json_file_one(self, file_path='employee_details_one.json'):
        """
        Converts the calling instance of Employee to JSON using the to_json method,
        and writes it to a file specified by the file_path parameter.
        """
        json_data = self.to_json()
        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)

    @staticmethod
    @log_execution_time
    def to_json_file_list(employees, file_path='employee_details_list.json'):
        """
        Converts a list of Employee objects to JSON,
          and writes the data to a file specified by the file_path parameter.
        If no file_path is provided, it defaults to 'employee_details_list.json'.
        """
        json_data = [employee.to_json() for employee in employees]
        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)

    @staticmethod
    @log_execution_time
    def to_json_file_all(employees, file_path='employee_details_all.json'):
        """
        Converts a list of Employee objects to JSON, 
        and writes the data to a file specified by the file_path parameter.
        If no file_path is provided, it defaults to 'employee_details_all.json'.
        """
        json_data = [employee.to_json() for employee in employees]
        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)


# Example usage:
if __name__ == "__main__":
    # Creating an Employee object and writing its JSON data to a file
    employee1 = Employee()
    employee1.emp_name = "John Doe"
    employee1.to_json_file_one()

    # Generating a list of Employee objects and writing their JSON data to a file
    employee_records = [Employee() for _ in range(50)]
    Employee.to_json_file_list(employee_records)

    # Generating a list of Employee objects and writing JSON data for all employees to a file
    all_employees = [Employee() for _ in range(100)]
    Employee.to_json_file_all(all_employees)
