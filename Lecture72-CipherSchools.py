# Chapter 3 Summary

# if statement
name = "Chandra Shekhar"
if name == "Chandra Shekhar" or name == "chandra shekhar":
  print("You are Chandra Shekhar")
elif name == "Rohit" or name == "rohit":
  print("You are Rohit")
else:
  print("You are not Chandra Shekhar")


# While loop
i=1
while i<=10:
  print(i + "Hello World")
  i += 1


# for loop
for i in range(1,11):
  print(i)

# for loop with step 2
for i in range(1,11,2):
  print(i)

# break keyword
for i in range(1,11):
  if i==5:
    break
  print(i)


# continue keyword
for i in range(1,11):
  if i==5:
    continue
  print(i)


# for loop with string
for i in "Chandra Shekhar":
  print(i)
