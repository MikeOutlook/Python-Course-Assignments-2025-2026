wea=input("Enter today's weather: ")
pm=int(input("Enter today's PM2.5 value: "))
if wea!="rain" and pm<75:
    print("Go outdoor for exercise")
else:
    print("Go to library to study")
