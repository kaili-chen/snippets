# Python 3

### Task
# Input Format: First line of the input contains an integer, N. Then N lines follow.
# All the characters in W are lowercase alphabet characters.
# Output format:
# 1. Print 1 if the conversation starts with *hackerrank*
# 2. Print 2 if the conversation ends with *hackerrank*
# 3. Print 0 if the conversation starts and ends with *hackerrank*
# 4. Print -1 if none of the above.
###

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def find_hackerrank(line):
    if line.startswith('hackerrank'):
        return 0 if line.endswith('hackerrank') else 1
    return 2 if line.endswith('hackerrank') else -1    
### MAIN
n = int(input())
for i in range(0,n):
    line = input()  # all input are in lowercase
    print(find_hackerrank(line))
