"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

list_of_numbers = []

# create a list of possible telemarketers
for call in calls:
    if '140' in call[0]:
        if call[0].index('140') == 0: # could use str.startswith()
            if call[0] not in list_of_numbers:
                list_of_numbers.append(call[0])

# remove from list the numbers which also received calls
for call in calls:
    if '140' in call[1]:
        if call[1].index('140') == 0:
            if call[1] in list_of_numbers:
                list_of_numbers.remove(call[1])

# remove from list the numbers which sent texts
for text in texts:
    if '140' in text[0]:
        if text[0].index('140') == 0:
            if text[0] in list_of_numbers:
                list_of_numbers.remove(text[0])
    if '140' in text[1]:
        if text[1].index('140') == 0:
            if text[1] in list_of_numbers:
                list_of_numbers.remove(text[1])

list_of_numbers.sort(key=int)

print "These numbers could be telemarketers:"

for number in list_of_numbers:
    print number

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

