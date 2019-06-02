"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_numbers_set = set()

def add_numbers_to_set(data_numbers):
    for number in data_numbers:
        unique_numbers_set.add(number[0])
        unique_numbers_set.add(number[1])

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


add_numbers_to_set(texts)
add_numbers_to_set(calls)
print("There are {} different telephone numbers in the records.".format(len(unique_numbers_set)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Big O' Notation:
We will get the numbers of the calls and the records.
Notation O(N)
"""