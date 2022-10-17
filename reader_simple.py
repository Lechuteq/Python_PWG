# Reading csv files v0.3
import csv
print()

''' First file open and printing '''

print("Print from file 1: ")

with open("list_a.csv", "r", newline='') as file1: 
    lines1 = file1.readlines()

#for line1 in lines1: 
#    print(line1)

#lines1 = lines1.()

print("Type of file 1: ", type(file1))
print("Type of lines1: ", type(lines1))
print(lines1)
print()
print(lines1[0])
'''
print("Print from file 2: ")

# Second file open and printing
with open("list_b.txt", "r") as file2: 
    lines2 = file2.readlines()

for line2 in lines2: 
    print(line2.rstrip())
'''

#print("Type of file 2: ", type(file2))
#print()

#print("Is differences: ", lines1 != lines2, )
#print()


file1.close()
#file2.close()
