l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_index_l1=[l1[i] for i in range(len(l1)) if i %2==1]
even_index_l2=[l2[i] for i in range(len(l2)) if i %2==0]
l3=odd_index_l1+even_index_l2
print(l3)