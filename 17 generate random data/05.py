import random
import string
def randomstring(stringlength):
    letters=string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringlength))
print("ramdom string is:",randomstring(5))    