wea=input("请输入今天天气：")
pm=int(input("请输入今天的PM2.5值："))
if wea!="雨" and pm<75:
    print("进行户外运动")
else:
    print("去图书馆学习")