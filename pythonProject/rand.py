import re

str1="random text generation, used in many reports"

matches=re.findall("in",str1)
print(matches)