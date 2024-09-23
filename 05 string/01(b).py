def middle_latter(s):
    len1=len(s)//2
    return s[len1-1]+s[len1]+s[len1+1]
    # return s[len1-1:len1+2] # string slicing

str1 = "JhonDipPeta"
str2 = "JaSonAy"

print(middle_latter(str1))
print(middle_latter(str2))