"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def equal_numbers(number1, number2):
    return number1 == number2

def get_unique_numbers(data_numbers):
    unique_numbers = []
    for i in range(len(data_numbers)):
        if i == 0:
            if equal_numbers(data_numbers[i][0], data_numbers[i][1]):
                unique_numbers.append(data_numbers[i][0])
            else:
                unique_numbers.append(data_numbers[i][0])
                unique_numbers.append(data_numbers[i][1])
        if(not (data_numbers[i][0] in unique_numbers)):
            unique_numbers.append(data_numbers[i][0])
        if(not (data_numbers[i][1] in unique_numbers)):
            unique_numbers.append(data_numbers[i][1])
    return unique_numbers

unique_numbers_text = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


unique_numbers_text = get_unique_numbers(texts)
unique_numbers_call = get_unique_numbers(calls)
final_unique_numbers = set(unique_numbers_call + unique_numbers_text)
print("There are {} different telephone numbers in the records.".format(len(final_unique_numbers)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Big O' Notation:
We will get the numbers of the calls and the records.
Notation O(3N)
"""