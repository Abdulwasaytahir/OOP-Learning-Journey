class Employee:
    language = "Py"  # This is a class attribute
    salary = 1200000

Wasay = Employee()
Wasay.name = "Abdul Wasay Tahir"
print(Wasay.name , Wasay.language , Wasay.salary)

Rafay = Employee()
Rafay.name = "Muhammad Rafay Tahir" # This is an instance attribute
print(Rafay.name , Rafay.language , Rafay.salary)

# Here name is an instance attribute and language and salary are class attributes as they directly belongs to the class
