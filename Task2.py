"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def equal_numbers(number1, number2):
    return number1 == number2

def get_unique_numbers(data_numbers):
    unique_numbers = {}
    for i in range(len(data_numbers)):
        if i == 0:
            unique_numbers[data_numbers[i][0]] = int(data_numbers[i][-1])
            unique_numbers[data_numbers[i][1]] = int(data_numbers[i][-1])
        if(data_numbers[i][0] in unique_numbers):
            unique_numbers[data_numbers[i][0]] = int(unique_numbers[data_numbers[i][0]]) + int(data_numbers[i][-1])
        else:
            unique_numbers[data_numbers[i][0]] =  int(data_numbers[i][-1])
        if(data_numbers[i][1] in unique_numbers):
            unique_numbers[data_numbers[i][1]] = int(unique_numbers[data_numbers[i][1]]) + int(data_numbers[i][-1])
        else:
            unique_numbers[data_numbers[i][1]] = int(data_numbers[i][-1])
    return unique_numbers

def get_longest_phonecall(list_phonecalls):
    maximum = max(list_phonecalls, key=list_phonecalls.get)
    return {maximum: list_phonecalls[maximum]}
longest_number = get_longest_phonecall(get_unique_numbers(calls))

def getKeyOfDictionary(dictionary):
    for key in dictionary:
        return key

def getValueOfDictionary(dictionary):
    for key in dictionary:
        return dictionary[key]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(getKeyOfDictionary(longest_number), getValueOfDictionary(longest_number)))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
Big O' Notation:
We will get the numbers of the calls and the records.
Notation O(2N^2)
"""