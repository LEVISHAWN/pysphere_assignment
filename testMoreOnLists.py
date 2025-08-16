mylist = [1, 2, 3, "Python", 3.14]

# Acess elements
print(mylist[3]) # Outputs Python

# Add elements
mylist.append("New item")
print(mylist) # adds "New item" at the end of the list

# Remove elements
mylist.remove(3.14) # Removes the first occurrence of 3.14
print(mylist)


#Check if an item exists
mylist2 = input("Enter item: ")
mylsit2 = input("Enter item: ")
if "Python" in mylist2:
    print("Python is in the list") # Outputs Python is in the list
else:
    print("Python is not in your list")

#List comprehension
squares = [x**2 for x in range(20)]
print(squares)