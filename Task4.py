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

unique_set_make_calls = set()
unique_set_receive_calls_texts = set()

# Ongoing calls
def get_ongoing_calls(list_numbers):
    for number in list_numbers:
        unique_set_make_calls.add(number[0])
        unique_set_receive_calls_texts.add(number[1])

def get_text(list_numbers):
    for number in list_numbers:
        unique_set_receive_calls_texts.add(number[0])
        unique_set_receive_calls_texts.add(number[1])

def print_list(list_numbers):
    for number in list_numbers:
        print(number)

get_ongoing_calls(calls)
get_text(texts)
sorted_possible_telemarketers = list(unique_set_make_calls.difference(unique_set_receive_calls_texts))
sorted_possible_telemarketers.sort()
print("These numbers could be telemarketers: ")
print_list(sorted_possible_telemarketers)

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

"""
Big O' Notation:
Notation O(N*logN)
"""
