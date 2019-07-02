"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

total_time = 0
telephone_number = ""
dated = ""

# Make a dictionary for all calls and their time

time_called = {}

for call in calls:
    if call[0] not in time_called.keys():
        time_called[call[0]] = int(call[3])
    else:
        time_called[call[0]] += int(call[3])

    if call[1] not in time_called.keys():
        time_called[call[1]] = int(call[3])
    else:
        time_called[call[1]] += int(call[3])


max_time_spent = max(zip(time_called.values(), time_called.keys()))

print(max_time_spent[1], "spent the longest time,", max_time_spent[0], "seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
