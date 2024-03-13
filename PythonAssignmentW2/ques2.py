"""Tabulate is an open-source python package/module, used to print tabular data"""
import time
from tabulate import tabulate

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

daysofWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


edict={}
def shortform(day):
    """this is used for slicing"""
    sf=day[0:3]
    return sf

for i in range(7):
    days_dict={
        daysofWeek[i]: (i+1,
                        shortform(daysofWeek[i]),
                        daysofWeek[i].lower(),
                        daysofWeek[i].upper(),
                        len(daysofWeek[i]))
    }
    #print(days_dict)
    edict.update(days_dict)

# print(dict)


@log_execution_time
def create_day_information(day_name):
    """this will create the data"""
    return [
        daysofWeek.index(day_name) + 1,
        day_name[:3],
        day_name.lower(),
        day_name.upper(),
        len(day_name)
    ]
# print(create_day_info())

days_table = []

for day_names in daysofWeek:
    days_table.append([day_names] + create_day_information(day_names))

# This will enerate the table
headers = ['Name of the Day', 'Occurrences', 'Short Form',
            'Name in Lower', 'Name in upper', 'Length']
print(tabulate(days_table, headers=headers, tablefmt='grid'))
