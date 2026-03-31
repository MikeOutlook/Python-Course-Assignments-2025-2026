hb=int(input("Enter hemoglobin value: "))
if hb >165:
    print("Hemoglobin elevated")
elif hb >120:
    print("Hemoglobin normal")
elif hb >91:
    print("Mild anemia")
elif hb >61:
    print("Moderate anemia")
elif hb >30:
    print("Severe anemia")
else:
    print("Extreme anemia")
