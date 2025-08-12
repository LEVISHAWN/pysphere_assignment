name = input("What is your name: ") #The variable here calls a string Levi
age = int(input("What is your age: ")) #The variable here calls an integer

if age <= 25:
    is_student = True
else:
    is_student = False

print(name, str(age), is_student)