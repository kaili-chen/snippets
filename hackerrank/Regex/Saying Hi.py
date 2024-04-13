# Python 3

### Task
# Given a sentence, s, write a RegEx to match the following criteria:
# 1. The first character must be the letter H or h.
# 2. The second character must be the letter I or i.
# 3. The third character must be a single space (i.e.: \s).
# 4. The fourth character *must not* be the letter D or d.
###

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def meets_criteria(line):
    criteria_pattern = r'^([Hh][Ii]\s[^Dd])'
    return re.match(criteria_pattern, line)

### MAIN
# read STDIN
n = int(input())
for i in range(0,n):
    line = input()  # all input are in lowercase
    if meets_criteria(line): print (line)
