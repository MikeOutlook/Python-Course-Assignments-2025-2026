info = "Patient male, 52 years old, diagnosed with diabetes"
print(info)
sex = info[2]
age = info[5:7]
diag = info[-3:]
print("Gender:", sex)
print("Age:", age)
print("Diagnosis:", diag)
print("This is a {} year old {} patient diagnosed with {}".format(age, sex, diag))