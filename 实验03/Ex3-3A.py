# Input data
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
# Calculate BMI
bmi = weight / (height ** 2)

if bmi <18:
    result="Underweight"
elif bmi <=25:
    result="Normal weight"
elif bmi <=27:
    result="Overweight"
else:
    result="Obese"

print("Your BMI is: {:.2f}, classified as {}".format(bmi,result))
