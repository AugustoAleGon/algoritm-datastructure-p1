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

# Define a function for getting fix numbers
def get_fixed_code(phonenumber):
    close_parenthesis = phonenumber.find(")")
    if(close_parenthesis != -1):
        return phonenumber[:(close_parenthesis+1)]

# Define a function for getting cellphone numbers
def get_cellphone_code(phonenumber):
  if(phonenumber.startswith('7') or phonenumber.startswith('8') or phonenumber.startswith('9')):
      return phonenumber[:4]



# Define a function for getting Bangalore's numbers
def get_bangalore_numbers(list_numbers):
  bangalore_codes = []
  total_calls = 0
  bangalore_fixed_calls = 0
  flag = True
  for number in list_numbers:
    if number[0].startswith("(080)"):
      if number[1].startswith("(0"):
        fix_code = get_fixed_code(number[1])
        if not fix_code in bangalore_codes:
          bangalore_codes.append(fix_code)
      if(number[1].find(" ") != -1):
        fix_code = get_cellphone_code(number[1])
        if not fix_code in bangalore_codes:
          bangalore_codes.append(fix_code)
      if(number[1].startswith("140") and flag):
        bangalore_codes.append("140")
        flag = False
    if number[0].startswith("(080)"):
      total_calls = total_calls + 1
    if number[0].startswith("(080)") and number[1].startswith("(080)"):
      bangalore_fixed_calls = bangalore_fixed_calls + 1
  bangalore_codes.sort()
  percentage = (bangalore_fixed_calls / total_calls) * 100
  return bangalore_codes, percentage

def print_list(list_numbers):
  for number in list_numbers:
    print(number)

print("The numbers called by people in Bangalore have codes:")
result = get_bangalore_numbers(calls)
print_list(result[0])

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(result[1]))
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Big O' Notation:
Notation O(N^2)
"""