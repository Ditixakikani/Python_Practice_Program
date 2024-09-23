start = 25
end = 50
print("Prime numbers between 25 and 50 are:")
for i in range(25,51):
    for j in range(2,i):
        if i % j==0:
            break
    else:
            print(i)