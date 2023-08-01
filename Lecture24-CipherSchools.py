# Two inputs
name = input("Enter your name: ")
age = input("Enter your age: ")

name,age=input("Enter your name and age: ").split()
print(name)
print(age)
# Enter your name and age: ChandraShekhar 22
# ChandraShekhar
# 22


name,age=input("Enter your name and age: ").split(",")
print(name)
print(age)
# Enter your name and age: Chandra Shekhar,22
# Chandra Shekhar
# 22
