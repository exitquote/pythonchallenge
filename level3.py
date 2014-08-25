import re
myfile = open('chars2.txt')
contents = myfile.read()
pattern = re.compile('[a-z0-9]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z0-9]{1}')
res = pattern.findall(contents)
print res