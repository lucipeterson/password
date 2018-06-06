#password.py
import random
import string
l = int(input("How many letters? "))
n = int(input("How many numbers? "))
p = int(input("How many punctuation marks? "))

password = ''
for i in range(0, l):
    password += random.choice(string.ascii_letters)
for i in range(0, n):
    password += random.choice(string.digits)
for i in range(0, p):
    password += random.choice(string.punctuation)


print(password)

another = input("Generate another password? ")
while another.lower() == "yes":
        l = int(input("How many letters? "))
        n = int(input("How many numbers? "))
        p = int(input("How many punctuation marks? "))

        password = ''
        for i in range(0, l):
            password += random.choice(string.ascii_letters)
        for i in range(0, n):
            password += random.choice(string.digits)
        for i in range(0, p):
            password += random.choice(string.punctuation)

        print(password)
        another = input("Generate another password? ")
