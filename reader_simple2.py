# Reading csv files v0.6 - DictReader approach
import csv

keys = ['name', 'family', 'house', 'id']

''' First file open and printing '''
#print("Print persons from list 1: ")

id_list1 = []

with open("students_a.csv", "r", newline='') as file1: 
    persons1 = csv.DictReader(file1, fieldnames=keys)
    for person1 in persons1:
        id_list1.append({   "name": person1['name'], 
                            "family": person1['family'], 
                            "house": person1['house'],
                            "id": person1['id'],
                        })
    

print(id_list1)



''' Second file open and printing '''
#print("Print persons from list 2: ")

with open("students_b.csv", "r", newline='') as file2: 
    persons2 = csv.DictReader(file2, fieldnames=keys)
    # for person2 in persons2:
    #    print(person2)


print()
#print(person1, type(person1))
#print(persons1, type(persons1))
#print(file1, type(file1))