#!/usr/bin/env python
#Author:Aditya kamat

f= open("sub.txt")
str1 = f.read()
lis = str1.split()
final_list = []

for i in range(0,len(lis),2):
	final_list.append(lis[i])
	
for x in sorted(final_list):
	print x
