#test
IDno=input("请输入就诊者的身份证号码：\n")
birth=IDno[6:10]
age=2025-int(birth)
print("就诊者{}岁".format(age))