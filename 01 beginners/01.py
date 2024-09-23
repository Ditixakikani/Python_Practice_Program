def sum_mul(num1,num2):
    product = num1*num2

    if product <= 1000:
        return product
    else: 
        return num1+num2

print(sum_mul(20,30))
print(sum_mul(30,40))