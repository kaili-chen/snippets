# Python 3

### Task
# Match test string S to pattern Xxxxx, where x denotes a word character and X denotes a digit
# S must start with a digit X and end with a . symbol
# S should be 6 characters long only.
###

Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
