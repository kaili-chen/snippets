# Python 3

### Task
# Match the pattern XXxXXxXX, where X denote a non-whitespace characters and x denote a whitespace characters
###

Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
