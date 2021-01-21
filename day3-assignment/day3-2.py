#Write a Python program to remove all duplicates words from a given sentence#
s = " sunfeast is brand of itc and classmate is also  brand of itc" 
l = s.split()
k = []
for i in l:
    if(s.count(i)>1 and (i not in k)or s.count(i)==1):
       k.append(i)
print(' '.join(k))