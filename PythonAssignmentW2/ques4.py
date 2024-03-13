"""generating fake data and performing certain tasks on it"""
import pandas as pd
from faker import Faker
import time
from collections import Counter
def log_execution_time(func):
    """log exceution"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("execution_logs.txt", "a",encoding="utf-8") as f:
            f.write(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds\n")
        return result
    return wrapper

fake = Faker()
data = []
for e in range(50):
    # looping in the given range to have fake data for 50 people
    emp_id = fake.unique.random_number(digits=5)
    emp_name = fake.name()
    emp_email = fake.email()
    business_unit = fake.random_element(elements=('HR', 'Finance', 'IT', 'Sales'))
    salary = fake.random_number(digits=5)
    data.append([emp_id, emp_name, emp_email, business_unit, salary])

# Save DataFrame to Excel
df = pd.DataFrame(data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
df.to_excel("Employee_Personal_Details.xlsx", index=False)

@log_execution_time
def get_employee_with_top_salary():
    """WAF to return the empolyee name with top most salary"""
    df = pd.DataFrame(data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    max_salary_row = df[df['Salary'] == df['Salary'].max()]
    return max_salary_row['EMP NAME'].iloc[0]

print("Emplyee With top salary: ",get_employee_with_top_salary())

@log_execution_time
def get_business_unit_with_top_salary():
    """WAF to return the Business Unit with top most aggregated salary"""
    df = pd.DataFrame(data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    aggregated_salary = df.groupby("Business Unit")["Salary"].sum()
    max_aggregated_salary = aggregated_salary.max()
    top_business_unit = aggregated_salary[aggregated_salary == max_aggregated_salary].index[0]
    return top_business_unit

print("Business unit with top salary: ",get_business_unit_with_top_salary())

@log_execution_time
def get_employee_with_top_salary_per_business_unit():
    """WAF to return the employee name in each Business Unit with top most salary"""
    df = pd.DataFrame(data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    top_employees = df.groupby("Business Unit").apply(lambda x: x.nlargest(1, "Salary"))
    return top_employees[["Business Unit", "EMP NAME"]]

print("Employees with top salary per BU: ",get_employee_with_top_salary_per_business_unit())

@log_execution_time
def delete_employee_with_least_salary():
    """WAF Delete the Record of the Employee name from the Excel File with the least salary."""
    df = pd.DataFrame(data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    min_salary = df["Salary"].min()
    df = df[df["Salary"] != min_salary]
    df.to_excel("Employee_Personal_Details.xlsx", index=False)

print("least_salary: ",delete_employee_with_least_salary())
