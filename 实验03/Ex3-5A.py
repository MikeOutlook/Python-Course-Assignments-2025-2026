genderList = ["Mrs","Mr"] # Create gender list
IDcard = input("Enter ID number: ")
gender = int(IDcard[-2]) # Extract second to last digit
genderID = gender % 2 # Get remainder
greet = genderList[genderID] # Index data from gender list using remainder
print(greet,"Hello")
