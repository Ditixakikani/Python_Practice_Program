def find_count(simple_str):
    # char_count=0
    # digit_count=0
    # symbol_count=0
    for char in find_count:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1  
str1 = "P@#yn26at^&i5ve"
print("total count char,digitand symbol")
find_count(str1)
                
