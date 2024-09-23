word=input('enter word')
print("Original String:",word)
x=len(word)
print("Printing only even index chars")
for i in range(0,x,2):
    print("index[", i, "]", word[i])
