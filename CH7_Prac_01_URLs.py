import re, pyperclip

# find URLs that begin with http:// or https://

# create a regex
httpRegex = re.compile(r'''
((http://|https://)\w+ # match http:// or https:// ((http://|https://) or word characters (\w) but there has to be at least one match (+)
\. # this is the period before TLD
(com|net|org|gov))    # choose either .com, .net, or .org
''', re.VERBOSE)

text = pyperclip.paste() # paste contents of clipboard to text variable
found_URL = httpRegex.findall(text) # returns match objects based on strings in text variable and stored match objects in found_URL variable

# clean up the output by iterating through each tuple from found_URL and extracting only the first item
all_URLs = [] # initialize all_URLs variable with an empty list
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
