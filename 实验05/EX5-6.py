# Create herb list, complete the following line
herbs_list =["Dexamethasone","Aminophylline","Lobelin","Bromhexine","Dextromethorphan"]
# Create herb stock list, complete the following line
stock_list =[30,40,33,34,28]
# Get user input for number, convert to integer, complete the following line
num =int(input("Enter the drug number to use: "))
# Get herb name from list, complete the following line
user_herbs =herbs_list[num-1]
# Get user input for quantity, convert to integer, complete the following line
quantity =int(input("Enter the quantity needed: "))
if quantity>stock_list[num-1]: # If stock is insufficient, display "Insufficient stock!"
    print("Insufficient stock!")
else:
    print("Stock meets demand!") # Otherwise, take the required quantity. Complete the following branch structure code



# Display current stock of required herbs, complete the following line
print()
