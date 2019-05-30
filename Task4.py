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

# Ongoing calls
def get_ongoing_calls(list_numbers):
    ongoing_calls = []
    for number in list_numbers:
        if number[0].startswith("140") and (not number[1].startswith("140")):
            if not number[0] in ongoing_calls:
                ongoing_calls.append(number[0])
    return ongoing_calls

def remove_telemarketers_sms(list_messages, ongoing_calls):
    for message in list_messages:
        if message[0].startswith("140"):
            if message[0] in ongoing_calls:
                ongoing_calls.remove(message[0])
        if message[1].startswith("140"):
            if message[1] in ongoing_calls:
                ongoing_calls.remove(message[1])
    ongoing_calls.sort()
    return ongoing_calls

telemarketeres_calls = get_ongoing_calls(calls)
telemarketers_set = remove_telemarketers_sms(texts, telemarketeres_calls)
final_result = set(telemarketers_set)

def print_set(set_numbers):
    for number in set_numbers:
        print(number)


print("These numbers could be telemarketers: ")
print_set(telemarketers_set)


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
Notation O(6N)
"""
