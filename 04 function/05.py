def fun(a,b):
    def addition(a,b):
         sum=a+b
         return sum
    return addition(a,b)+5

num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
print(fun(num1,num2))

# print(fun(5,10)) 


