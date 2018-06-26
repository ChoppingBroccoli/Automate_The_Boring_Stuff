import re

'''
WORK IN PROGRESS.
Regex's work but the if statements do not


Identify SSNs & CCs
Replace with "REDACTED"

'''

user_input = input('Enter a number: ')

# Regex
# SSN: xxx-xxx-xxxx
#SSN_Regex = re.compile(r'\d{3}-\d{3}-\d{4}')
SSN_Regex = re.compile(r'\d{3}-\d{3}-\d{4}')
SSN_Test = SSN_Regex.search(user_input)

# IF statement not working right. Traceback error if there is no match
if SSN_Test == 'None':
    print('No match found')
else:
    print('Serial Number:', SSN_Test.group())
    



'''
# Regex
# CC: xxxx-xxxx-xxxx-xxxx
CC_Regex = re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}')
CC = CC_Regex.findall(user_input)

if CC != None:
    print('Credit Card Number:', CC)
else:
    print('No match found')

'''
