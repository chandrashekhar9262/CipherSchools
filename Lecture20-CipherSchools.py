# String Concatenation
first_name="Chandra Shekhar"
last_name="Kumar"
full_name = first_name +" "+ last_name
print(full_name)
# Output : Chandra Shekhar Kumar


# String can be concate with Strings only
# String cannot be cancate with numbers
# Example:

print(full_name + 3)
# TypeError

# We can do as below:
print(full_name + "3")
print(full_name + str(22))
