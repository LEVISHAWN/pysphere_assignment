# # We are going to learn more about If statements
# age = int(input("What is your age: "))
# member = input("Are you a member: ")

# if age <= 18:
#     print("You can't vote this year. ")

# elif age > 18 <= 65 and member == "Yes":
#     print("You can vote and you are a member")

# elif age > 18 <= 65 and member == "No":
#     print("You can vote but not a member. ")

# elif age > 65 and member == "No":
#     print("You can't vote and you are a member. ")

# else:
#     print("You are not a member and you can't vote. ")


# Nested If-Statements
score = int(input("What is the student's score: "))

if score >= 50:
    print("You have passed. ")
    if score >= 90:
        print("Exceeded expectations. ")
    elif score >= 75 < 90:
        print("You have reached expectations. ")
    else:
        print("You have done well but try do better")
else:
    print("You have failed.")
