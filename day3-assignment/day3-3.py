#Write a Python program to find all occurrences of a character in the given string# Python3 code to demonstrate 

# initializing string 
str1 = "letsupgrade  gives training on pythone essentials"

 
# counting e 
count = 0

for i in str1: 
	if i == 'e': 
		count = count + 1

# printing result 
print ("Count of e in str1 is : "
	+ str(count)) 
