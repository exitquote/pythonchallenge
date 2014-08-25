import re
from os import getcwd
from os import listdir
import zipfile
# unzip the channel file and list all its contents
zipper = zipfile.ZipFile('channel.zip')
for onefile in zipper.namelist():
	extractdir = getcwd() + "/channel/"
	zipper.extract(onefile, extractdir)
files = listdir(getcwd()+"/channel/")
# it's basically a big linkedlist.
# let's assume we'll need to run through all of them
total = len(files)
# pattern to find the next item in the list
pattern = re.compile('ext nothing is \d{1,10}')
# pattern to get just the number out of this
nums = re.compile('\d{1,10}')
# get the linkedlist head
# open "readme.txt" and get "start from" line for the file name
readmepattern = re.compile('start from \d{1,10}')
readme = open(getcwd()+"/channel/readme.txt")
for line in readme:
	startnum = readmepattern.findall(line)
	if startnum:
		starter = nums.findall(startnum[0])
		newfile = starter[0]+".txt"
# if we have the head, run through and get all the comments
if (newfile):
	numlist = list()
	comm = ''
	x = 0
	while x < len(files):
		nextfile = open(getcwd()+"/channel/"+newfile)
		text = nextfile.readline()
		res = pattern.findall(text)
		try:
			next = nums.findall(res[0])
			newfile = next[0]+'.txt'
			numlist.append(next[0])
			info = zipper.getinfo(newfile)
			comm += info.comment
		except IndexError:
			break
		x = x + 1
	print comm
else:
	print "error"
