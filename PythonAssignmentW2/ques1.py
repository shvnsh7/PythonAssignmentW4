"""import time"""
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

days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
@log_execution_time
def generate_consecutive_days(day):
    """consecutive days"""
    return [(days_of_week[i], days_of_week[i+1]) for i in range(len(days_of_week)-1)]

@log_execution_time
def create_day_info_dict(day):
    """create lower upper etc"""
    day_info_dict = {}
    for i, day in enumerate(days_of_week, start=1):
        day_info_dict[day] = (i, day[:3], day.lower(), day.upper(), len(day))
    return day_info_dict

@log_execution_time
def count_char_occuerrenvces(day):
    """count"""
    return tuple((day, Counter(day)) for day in days_of_week)

print("list of tuples which has the two consequtive days grouped together")
print(generate_consecutive_days(days_of_week))
print("\nDictionary with day information")
print(create_day_info_dict(days_of_week))
print("\ntuple with all the characters and their number of occurences in each name of the day.")
print(count_char_occuerrenvces(days_of_week))
