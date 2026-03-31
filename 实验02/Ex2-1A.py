# test
id_no = input("Enter patient ID number:\n")
birth = id_no[6:10]
age = 2025 - int(birth)
print("Patient is {} years old".format(age))