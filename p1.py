import re
str = "examination"
pattern = re.compile("a\w\w\w")
print(pattern.findall(str))
print(pattern.sub("yyy", str))
print(pattern.split(str))