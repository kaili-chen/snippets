# ruby 
# Forward reference is supported by JGsoft, .NET, Java, Perl, PCRE, PHP, Delphi and Ruby regex flavors.

### Task
# Write a regex which will match test string S, with following condition(s):
# - S consists of "tic" or "tac".
# - "tic" should not be immediate neighbour of itself.
# - The first "tic" must occur only when "tac" has appeared at least twice before.
###

Regex_Pattern = '^(\2tic|(tac))*$'

print !!(gets =~ /#{Regex_Pattern}/)
