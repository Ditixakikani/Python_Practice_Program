
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for a,b in zip(list1,list2[::-1]):
    print(a,b)