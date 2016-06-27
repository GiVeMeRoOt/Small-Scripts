#!/usr/bin/env python
#Author:Aditya kamat

dict = {}

print "Taking  the file as input"

f = open("test.txt","r")

input = f.read()

print "Finished reading the file"

print "The file contents are: "

for i in input.strip():

	if i in dict.keys():
		dict[i] += 1
	else:
		dict[i] = 1

for i in dict.keys():
	print i+"    "+str(dict[i])


