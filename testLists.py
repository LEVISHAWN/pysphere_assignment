# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)

# print(mylist)

# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)

# for x in mylist:
#     print(x)

# List where user can input the number to be on the list
mylist = []
num_items = int(input("Enter number of items: "))

for x in range(num_items):
    item = input("Enter items {x+1}: ")
    mylist.append(item)

print("Items in the list: ")
for item in mylist:
    print(item)