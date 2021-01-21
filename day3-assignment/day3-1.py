#Write a Python program to remove empty List from List.
t_list = [4,7,[],8,[],[],9]
print("the original list is:"+ str(t_list))
res = list(filter(None,t_list))
print("list after empty list removal : " + str(res))