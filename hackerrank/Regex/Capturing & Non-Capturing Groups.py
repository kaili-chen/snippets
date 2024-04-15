# Python 3

### Task
# Write a regex which will match test string S with the following condition:
# - S should have 3 or more consecutive repetitions of "ok"
###

Regex_Pattern = r'(ok){3,}'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
