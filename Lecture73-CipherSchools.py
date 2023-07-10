# Functions in Python
# Ex: print(), len()

name="Chandra Shekhar"
print(len(name))

# we can create our own function using 'def' keyword

def add_two(a,b):
  return a+b

total=add_two(5,4)
print(total)

# or
print(add_two(5,6))


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
total = add_two(a,b)
print(total)


first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print(add_two(first_name, last_name))
