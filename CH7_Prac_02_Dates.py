'''
Clean up dates in different date formats (such as 3/14/2015, 03-14-2015,
and 2015/3/14) by replacing them with dates in a single, standard format.
'''

import re

'''
=================
++ Pseudo Code ++
=================
create a regex to identify dates in different formats
..possible date formats
...MM/DD/YYYY----DONE
...MM-DD-YYYY----DONE
...MM.DD.YYYY----DONE
collect the parts of the date (day, month, year)
put collected parts of the date in the correct format (dayMONTHyear)
'''


datesRegex = re.compile(r'''
(((\d\d-\d\d- | \d\d/\d\d/ | \d\d.\d\d.)) # matches xx-xx- or xx/xx/ xx.xx. and any variation thereof
(\d\d\d\d)) # matches xxxx(year)
''', re.VERBOSE)


mo = datesRegex.findall('14.08-2018')
print(mo)


'''
Need to find a way to only accept "/", "-", or "." not all 3
Need to substitute (sub()) and join to get the format I want (dayMONTHyear)
'''

