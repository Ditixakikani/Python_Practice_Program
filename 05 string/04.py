str1 = "PyNaTive"
print(str1)
lower=[]
upper=[]
for char in str1:
    if char.islower ():
        lower.append(char)
    else:
        upper.append(char)
sort=''.join(lower+upper)
print(sort)            
