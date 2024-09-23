print('Printing current and previous number sum in a range(10)')
previous_num=0      
for i in range(10):
    print(f"Current Number {i} Previous Number  {previous_num}  Sum: {previous_num*i} ")
    previous_num = i