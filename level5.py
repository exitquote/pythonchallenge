import pickle
filer = open('banner.p')
test = pickle.load(filer)
for item in test:
	outline = ''
	for thing in item:
		char = thing[0]
		num = thing[1]
		outline += char * num
	print outline