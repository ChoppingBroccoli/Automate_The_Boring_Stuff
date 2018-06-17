#! /usr/bin/python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
# Since there are groups, findall() will return a list of tuples for the phone numbers.
# A fix for this is to put the entire regex into a group.
(
((\d\d\d) | (\(\d\d\d\)))? # area code (optional)(3 digits no parens OR 3 digits with parens)
(\s | -) # first separator (space OR hyphen)
\d\d\d # first 3 digits
- # separator
\d\d\d\d #last 4 digits
(((ext(\.)?\s) | x) # extenstion with verbiage (optional)('ext' with/without a period OR just an 'x')
(\d{2,5}))? # extension only digits (optional)(between 2 - 5 digits)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# name@domain.com (include .+_-)

[a-zA-Z0-9_.+-]+	# name part
@ # @ symbol
[a-zA-Z0-9_.+-]+ # domain part
''', re.VERBOSE)

# Get text off the clipboard
text = pyperclip.paste()

# Extract email/phone number from the text
phoneRegex.findall(text) # returns a list of strings

# Copy extracted email/phone to the clipboard
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
