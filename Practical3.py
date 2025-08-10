# Detect if user has passed pysical
#  fitness of the recruitment. 
# Condition: Any male below height
#  of 60inches is disqualified and
#  female below 58inches is disqualified.


height = float(input("Enter your height: "))
gender = input("Enter your gender: ")

if gender == "male" and height < 60:
    print("You are disqualified")
elif gender == "female" and height < 58:
    print("You are disqualified: ")
else:
    print("You are qualified: ")