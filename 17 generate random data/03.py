import secrets
secretsgenrator=secrets.SystemRandom()
otp=secretsgenrator.randrange(100000,999999)
print("secure random is: ",otp)