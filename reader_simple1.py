# Reading csv files v0.5 - DictReader approach
import csv

keys = ['Key_1', 'Key_2', 'Key_3']

''' First file open and printing '''

print("Print from file 1: ")

with open("list_a.csv", "r", newline='') as file1: 
    dictionary1 = csv.DictReader(file1, fieldnames=keys)
    for row in dictionary1:
        print(row['Key_1'], row['Key_2'], row['Key_3'])


print()
print("Type of data: ", dictionary1.dialect)
print("Lines readed: ", dictionary1.line_num)
print("Fieldnames:   ", dictionary1.fieldnames)
#print("Type of file 1: ", type(file1))
#print("Type of dictionary1: ", type(dictionary1))

#l = list(dictionary1())
#print(l)


file1.close()

