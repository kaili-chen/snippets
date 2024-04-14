# Python 3

### Task
# Match pattern: xxxXxxxxxxxxxxXxxx, where x denotes any word character and X denotes any non-word characters
###

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
