myfile = open('chars.txt')
contents = myfile.read()
letters = {}
for letter in contents:
	if letter not in letters:
		letters[letter] = 1
	else:
		letters[letter] = letters[letter]+1
print letters
