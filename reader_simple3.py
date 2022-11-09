# Reading csv files v0.7 - DictReader new approach
import csv

#keys = []

with open("students_a.csv", "r", newline='') as header:
    row = csv.reader(header)
    keys = next(row)

print(f"Keys for dictionary: {keys}")


id_list1 = []

with open("students_a.csv", "r", newline='') as file1: 
    persons1 = csv.DictReader(file1, fieldnames=keys)
    for person1 in persons1:
        id_list1.append({   "Name": person1['Name'], 
                            "Family": person1['Family'], 
                            "House": person1['House'],
                            "Id": person1['Id'],
                        })

print(person1)
print(f"Type of id_list1: {type(id_list1)}")
print()
print(id_list1[1])