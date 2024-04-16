# Python 3

### Task
# Write a regex that can match all occurrences of o followed immediately by oo in test string S.
###

Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
