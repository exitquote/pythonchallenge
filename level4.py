import urllib
import re
baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682')
text = page.read()
pattern = re.compile('the next nothing is \d{1,10}')
nums = re.compile('\d{1,10}')
res = pattern.findall(text)
x = 0
print res
while x < 300:
	try:
		phrase = nums.findall(res[0])
		print phrase
		url = baseurl+phrase[0]
		print url
		page = urllib.urlopen(url)
		text = page.readline()
		res = pattern.findall(text)
		x = x + 1
	except IndexError:
		x = 300
		print "done"
