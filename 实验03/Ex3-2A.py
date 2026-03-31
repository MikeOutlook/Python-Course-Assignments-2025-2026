# Hypertension diagnosis
SBP = int(input("Enter systolic blood pressure: "))
DBP = int(input("Enter diastolic blood pressure: "))
if (SBP >= 140) or (DBP >= 90):
    print("Patient has hypertension")
else:
    print("Patient does not have hypertension")
