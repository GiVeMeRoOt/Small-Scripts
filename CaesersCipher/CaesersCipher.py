#!/usr/bin/env python
#Author:Aditya kamat
#Caesers shift ciphers...Type the encrypted message as input1

input1 = "xliwigvixtewwtlvewimwewtlonvlbuuihprubmdpcomvxkjxkd"

for i in range(26):
	c = ""
	for j in input1:
		n = ord(j)		
		if (n>64 and n<91): 
			n=n+i
			if n>90:
				n = 96+(n-90)
		elif (n>96 and n< 123):
			n=n+i
			if n>122:
				n = 64+(n-122)
		c = c+chr(n)
	print "Rotation:"+str(i)+"\t\t"+"String: "+c+"\n"	
	







			