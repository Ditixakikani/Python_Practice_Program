def tax(pay):
    if pay <= 10000:
        tax = 0
    elif pay <= 20000:
        tax = (pay-1000)*0.1
    else:
        tax = 10000*0.0
        tax += 10000*0.1
        tax += (pay-20000)*0.2
    return tax

pay=int(input("enter pay:"))
print(f"your tax is:{tax(pay)}")          
    