# Function practice in Python
def last_char(name):
  return name[-1]
print(last_char("Chandra Shekhar"))
# Output: r

print(last_char(9))       # it will return error


# def odd_even(num):
#   if num%2 == 0:
#     return "even"
#   else:
#     return "odd"

def odd_even(num):
  if num%2 == 0:
    return "even"
  return "odd"

print(odd_even(9))
# Output: odd
print(odd_even(10))
# Output: even


def is_even(num):
  if num%2 == 0:
    return True
  else:
    return False
print(is_even(10))
# Ouput: True
# Or 
def is_even(num):
  return num%2 == 0
print(is_even(9))
# Output: False

def song():
  return "Hanuman Chalisa"
print(song())
