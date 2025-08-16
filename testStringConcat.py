first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
full_name = first_name + " " + last_name
print(full_name) #this outputs hte full name concatenated from first and last name

# String formating
age = input("What is your age: ")
info = f"{full_name} is {age} years old."
print(info) #this output full name and age concatenated in a formatted string
