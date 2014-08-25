import string
str = "map"
outstring = ''
str1 = string.lowercase
str2 = str1.replace(str1[:2], '')+str1[:2]
table = string.maketrans(str1, str2)
outstring = string.translate(str, table)
print outstring
