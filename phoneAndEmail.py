#! python3
# phoneAndEmail.py - Finds phone number and email addresses

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # optional area code \d\d\d or (\d\d\d)
(\s|-|\.)?         # optional separator space (\s) or hyphen or period
(\d{3})            # first 3 digits
(\s|-|\.)          # separator space (\s) or hyphen or period
(\d{4})            # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # optional extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-z0-9-_.]+    # username
@               # @ symbol
[a-z0-9-_.]+    # domain name
(\.[a-z{2,4})   # TLD
)''', re.VERBOSE;re.IGNORE)



# TODO: Find matches in clipboard text

# TODO: Copy results to the clipboard
