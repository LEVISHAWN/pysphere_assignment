# Sets are unordered collection of unique elements defined by values separated by commas inside CURLY BRACES{}
myset = {1, 2, 3, 4, 5, 5, 3, 3 }
print(myset) # Any duplicates are removed.
 
 # Adding and removing of sets

myset.add(20)
myset.add(75)
print(myset) # This adds 20 and 75 to the set

myset.remove(5)
myset.remove(3)
print(myset) # This removes 5 and 3 from the set