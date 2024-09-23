def palindrome(num):
    print(f"Number is {num}")
    if str(num)==str(num)[::-1]:
        return"palindrome"
    return"not palindrome"


a=int(input("enter number :"))
print(palindrome(a))