# Python 3

### Task
# For every API request given in input, print "VALID" if it has a valid language string, else print "INVALID"
# Valid languages: C, CPP, JAVA, PYTHON, PERL, PHP, RUBY, CSHARP, HASKELL, CLOJURE, BASH, SCALA,  ERLANG, CLISP, LUA, BRAINFUCK, JAVASCRIPT, GO, D, OCAML, R, PASCAL, SBCL, DART,  GROOVY, OBJECTIVEC
# Input format: first lines contains N, N API requests follows
# Each request has an integer api_id and a string language which are the request parameters placed by the an API request.
###

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def has_valid_lang(submission):
    lang_pattern = r'\b(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA| ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART| GROOVY|OBJECTIVEC)\b'
    return re.search(lang_pattern, submission) is not None
    
### MAIN
# read STDIN
n = int(input())
for i in range(0,n):
    submission = input()
    print('VALID') if has_valid_lang(submission) else print('INVALID')
