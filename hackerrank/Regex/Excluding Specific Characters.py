# Python 3

### Task
# Match test string S with the following conditions:
# - must be of length 6
# - First character should not be a digit
# - Second character should not be a lowercase vowel
# - Third character should not be b, c, D or F
# - Fourth character should not be a whitespace character
# - Fifth character should not be a uppercase vowel
# - Sixth character should not be a . or , symbol.
###

Regex_Pattern = r'^[^0-9][^aeiou][^bcDF]\S[^AEIOU][^\.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
