levi = (1, 2, 3, "Pysphere")
print(levi[3])

# Attempting to modify a tuple
levi.append("Mugendi")
print(levi)


#Tuple modification leads to an error....(
#   File "/home/levi/Downloads/pysphere_assignment/testTuples.py", line 4, in <module>
#     levi.append("Mugendi")
#     ^^^^^^^^^^^
# AttributeError: 'tuple' object has no attribute 'append')
