import re, pyperclip

# find URLs that begin with http:// or https://

# create a regex
httpRegex = re.compile(r'''
((http://|https://)\w+ # determine http:// or https://
\. # period before TLD
(com|net|org|gov))    # choose either .com, .net, or .org
''', re.VERBOSE)

text = pyperclip.paste() # paste contents of clipboard
found_URL = httpRegex.findall(text) # returns match objects

# clean up the output by iterating through each tuple from found_URL to extract only the first item
all_URLs = []
for each_URL in found_URL:
    all_URLs.append(each_URL[0])

# test if any URLs were found
if len(all_URLs) == 0:
       print('No URLs found')
else:
    results = '\n'.join(all_URLs) + '\n'
    print('Results: ' + '\n' + results)

'''
Test Data
http://google.com
https://itvantage.com
http://tshirthell.com
https://wellsfargo.org
https://whitehouse.gov
'''
