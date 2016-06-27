#!/usr/bin/env python
#Author:Aditya kamat
#To check if a set of characters exist in a single word in the dictionary and if the size of the word is the same as the number of characters

f = open("../wordlist","r")
char = ['a', 'e', 'i', 'l', 'q', 'u', 't', 'y']
for i in f.readlines():
	for j in char:
		if j in i:
			continue
		else :
			break
	else:
		if len(char) == len(i.strip()):
			print i

