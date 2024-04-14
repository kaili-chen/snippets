# Python 3

### Task
# Write a regex that will match test string S using the following conditions:
# - S should begin with 2 or more digits
# - After that,  should have 0 or more lowercase letters
# - should end with 0 or more uppercase letters
### 

Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
