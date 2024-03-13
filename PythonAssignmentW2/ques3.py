"""pandas is a data manipulation package in Python for tabular data"""
import pandas as pd
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

daysofWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

edict={}
@log_execution_time
def short_form(day):
    """this function is for the slicing day """
    sf=day[0:3]
    return sf

for i in range(7):
    days_dict={
        daysofWeek[i]: (i+1,short_form(daysofWeek[i])
                        ,daysofWeek[i].lower(),daysofWeek[i].upper(),len(daysofWeek[i]))
    }
    #print(days_dict)
    edict.update(days_dict)

#print(dict)

df = pd.DataFrame.from_dict(dict, orient='index',
                            columns=["Occurences",
                                      "Short Form",
                                        "Name in Lower",
                                          "Name in Upper",
                                            "Length"])
df.to_excel("days_info.xlsx", index_label="Name of the Day")
