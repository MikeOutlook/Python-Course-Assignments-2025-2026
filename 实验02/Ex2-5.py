month_str = "JanFebMarAprMayJunJulAugSepOctNovDec"
a = int(input("Enter month number: "))
b = month_str[(a-1)*3:a*3]
print(b)