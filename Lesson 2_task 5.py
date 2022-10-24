

# 5.Write a Python program to find largest number among three numbers entered by user

list_= []
for i in range(3):
    list_.append(int(input()))
list_.sort()
print(list_[-1])
