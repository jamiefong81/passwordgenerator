

import random
choices = "1234567890!@#$%^&*()qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKZXCVBNM"
password = ""

print ("Password Length?")
userLength = input()
userLength = int(userLength)

for i in range(userLength):
    password += random.choice(choices)

print (password)
