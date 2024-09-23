def add_middle(str1,str2):
    l1=len(str1)//2
    return str1[0:l1]+str2+str1[l1:]

s1 = "Ault"
s2 = "Kelly"
print(add_middle(s1,s2))

