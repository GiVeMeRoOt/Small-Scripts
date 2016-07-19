#!/usr/bin/env python
#Author:Aditya kamat

import PyPDF2
##Type in the name of the pdf file in place of 'mypassword.pdf'
f = PyPDF2.PdfFileReader(file('mypassword.pdf', "rb"))

##Type in the path of your word list
wl = open('../wordlist')

for i in wl:
	i = i.strip()	
	print "Checking %s"%i
	if(f.decrypt (i)):
		print "success"
		break
	else:
		print "Failure"
		
print "Password is: %s"%i
