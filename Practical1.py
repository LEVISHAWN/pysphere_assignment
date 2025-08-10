# Practical Examples
# A hospital has called you to 
# create some python comp code to 
# differenciate between adults and 
# children. Given their age, every
# patient under 18 is regarded as a child


age = input("Enter your age: ")
age_int = int(age)

if age_int < 18:
    print("You are a minor")
elif age_int > 18 and age_int < 65:
    print("You are an adult")
else:
    print("You are a senior citizen")