#Exercise #1

#Create a list clothes = ["socks", "shirt", "skirt", "scarf"] and function insert_element():

clothes = ["socks", "shirt", "skirt", "scarf"]

def insert_element(new_cloth, index=0):
    clothes.insert(index, new_cloth)
    print(clothes)

insert_element('pants', 2)
insert_element("hat", -1)
insert_element("coat")


#Exercise #2

#Create a list employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"] and a function replace_employee():

employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
print("The original list : " + str(employee_shift))

new_employees = [item.replace("Kelly", "Maria") for item in employee_shift]

print("The list after substring replacement : " + str(new_employees))