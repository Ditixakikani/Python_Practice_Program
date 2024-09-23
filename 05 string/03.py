def start_add(str1,str2):
    l1=len(str1)//2
    l2=len(str2)//2
    return str1[0]+str2[0]+str1[l1]+str2[l2]+str1[-1]+str2[-1]


s1 = "America"
s2 = "Japan"
print(start_add(s1,s2))
