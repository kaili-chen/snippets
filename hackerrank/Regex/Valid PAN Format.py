# Python 3

### Task
# Your task is to figure out if the PAN number is valid or not. A valid PAN number will have all its letters in uppercase and digits in the same order as listed above.
# PAN Number format: <char><char><char><char><char><digit><digit><digit><digit><char>
# Each <char> is an uppercase letter
# Each <digit> lies between 0 and 9
# The length of of the PAN number is always 10
###

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def is_pan_number(pan_number):
    regex_pattern = r'[A-Z]{5}\d{4}[A-Z]{1}'
    return len(pan_number) == 10 and re.match(regex_pattern, pan_number) is not None
    
### MAIN
# read input
n = int(input())

for pan in range(0, n):
    pan_number = input()
    print('YES') if is_pan_number(pan_number) else print('NO')
