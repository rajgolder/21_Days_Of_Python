#variables in python

first_name = "Rek"
last_name = "Nitro"
age = 180
learning_python = True
skills = ["Python", "VS Code", "Github"]
person_info = {
    "first_name" : "Rek",
    "last_name" : "Nitro",
}

#printing the values stored in the variable

print("First name:", first_name)
print("First name length:", len(first_name))
print("Last name:", last_name)
print("Last name lenght:", len(last_name))
print("Age:", age)
print("Learning Python:", learning_python)
print("Skills:", skills)
print("Person information", person_info)

#declaring multiple variable in one line

first_name, last_name, age, learning_python = "Rek", "Nitro", 180, True
print("First name:", first_name)
print("Last name:", last_name)
print("Age:", age)
print("Learning Python:", learning_python)