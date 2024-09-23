def add(num):
    if num:
        return num+add(num-1)
    else:
        return 0
num1=int(input("enter a number:"))
print(add(num1))    
    