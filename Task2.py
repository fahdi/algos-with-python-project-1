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

for call in calls:
    if (int(call[3]) > total_time):
        total_time = int(call[3])
        telephone_number = call[0]
        dated = call[2]

date_obj = datetime.strptime(dated, '%d-%m-%Y %H:%M:%S') #01-09-2016 06:01:12 & 13-09-2016 16:11:06
month_year = date_obj.strftime("%B %Y")

print telephone_number, "spent the longest time,", total_time, "seconds, on the phone during", month_year, "."

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

