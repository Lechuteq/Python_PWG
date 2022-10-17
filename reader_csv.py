# Reading csv files v0.3
import csv
print()


print("Print from file 1: ")

with open("list_a.csv", "r", newline='') as file: 
    lines = file.readlines()

with open("list_b.csv", "r", newline='') as file_new: 
    lines_new = file_new.readlines()

print("Type of file: ", type(file))
print("Type of lines: ", type(lines))
print(lines)
print(lines_new)
print()
#print(lines[0])

#Check if there is difference
difference = []

for i in range(len(lines)):
    if lines[i] != lines_new[i]:
        print("Found diffrence in files.")
        difference = difference.append(lines_new[i])
        print(lines_new[i]) 
    #else:
    #print("No diffrence in files.")

file.close()

