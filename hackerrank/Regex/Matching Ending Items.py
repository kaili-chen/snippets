# Python 3

### Task
# Write a RegEx to match a test string, S , under the following conditions:
# - S should consist of only lowercase and uppercase letters (no numbers or symbols).
# - S should end in s
###

Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
