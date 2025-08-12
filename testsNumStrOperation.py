one = 1
two = 2
three = one + two
print(three)


hello = "Hello"
world = "World"
helloworld = hello + " " + world
print(helloworld)



a, b, c = 1, 2, 3
sum = a + b + c
print("Sum = ", sum)

# Wrong type of code concatenation
one = 1
two = 2
hello = "Hello"
print(one + two + hello)

#Correct code concatenation 1
one = 1
two = 2
hello = "Hello"
print(str(one) + str(two) + hello)

#Correct code concatenation 2
one = 1
two = 2
hello = "Hello"
print(f"{one}{two}{hello}")

#Correct code concatenation 3
one = 1
two = 2
hello = "Hello"
onestring = str(one)
twostring = str(two)

print(onestring + twostring + hello)