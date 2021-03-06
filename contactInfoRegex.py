#!usr/bin/env python3

""" Finds phone numbers and email addresses using regular expressions
    Uses the regex and pyperclip module.
    Based off the book Automate the Boring Stuff With Python
    Created by Keith Alpichi on Oct. 22, 2015.
"""

import pyperclip, re


# phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #separator space, "-" or "."
    (\d{3})                         #first three digits of number
    (\s|-|\.)?                      #separator
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension, match space or more, then "ext", "x", or "ext.", then a space or more then 2-5 digit ext.
    )''', re.VERBOSE)

# email address regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           #username matching one or more of either an a-z, A-Z, 0-9, ".", "_", "%", "+", "-"
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something could be ".io" to ".com"
)''', re.VERBOSE)

# find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails were found.')
