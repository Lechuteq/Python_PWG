# Reading csv files v0.8 - (list of dictionaries, exit when keys error)
import csv

print()

# Keys from file 1
with open("students_a.csv", "r", newline='') as header1:
    row = csv.reader(header1)
    keys1 = next(row)
print(f"Keys for dictionary1: {keys1}")

# Keys from file 2
with open("students_b.csv", "r", newline='') as header2:
    row = csv.reader(header2)
    keys2 = next(row)
print(f"Keys for dictionary2: {keys2}")

if keys1 == keys2:
    print("The same keys in both files.")
else: 
    print("Keys error !")
    exit()


# first file DictReader (reference file)
id_list1 = []

with open("students_a.csv", "r", newline='') as file1: 
    persons1 = csv.DictReader(file1, fieldnames=keys1)
    for person1 in persons1:
        id_list1.append({   "Name": person1['Name'], 
                            "Family": person1['Family'], 
                            "House": person1['House'],
                            "Id": person1['Id'],
                        })

# second file DictReader (refered file)
id_list2 = []

with open("students_b.csv", "r", newline='') as file2: 
    persons2 = csv.DictReader(file2, fieldnames=keys2)
    for person2 in persons2:
        id_list2.append({   "Name": person2['Name'], 
                            "Family": person2['Family'], 
                            "House": person2['House'],
                            "Id": person2['Id'],
                        })

#print(person1)
print(f"Type of id_list1: {type(id_list1)}")

# printing loop
#print("Elements from list: ")
#for i in range(len(id_list1)):
#    print(id_list1[i])

#print(id_list1[1])
#print()
#for i in range(len(id_list2)):
#    print(id_list2[i])

'''
for i in range(len(id_list1) - 1):
    print(id_list1[i + 1]["Id"])

for j in range(len(id_list2) - 1):
    print(id_list2[j + 1]["Id"])

'''