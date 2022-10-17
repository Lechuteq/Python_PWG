# Reading files v1.0
a = "Hello reader!"
print(a)


file1 = open("list_1.0.xml", "r", encoding="utf-8") # this is "UTF-8" file
#print(file.read())
file2 = open("list_1.1.xml", "r", encoding="utf-8")

#file1 = str(file1)

file = []

if file2 != file1: 
    file = file.append(file)

print(file1)

print("Type of file: ", type(file1))

file1.close()
file2.close()
#file = file.decode("UTF-8")

#for line in file.readlines():
#    print(line.strip())

