student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["favorite subject"] = input("Enter favorite subject: ")

print("\n")

for key,value in student.items():
    print(key.title()+":",value)
