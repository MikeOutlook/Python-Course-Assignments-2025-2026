# 输入数据
height = float(input("请输入身高,单位米： "))
weight = float(input("请输入体重,单位公斤： "))
# 计算身体质量指数
bmi = weight / (height ** 2)

if bmi <18:
    result="低体重 "
elif bmi <=25:
    result="正常体重 "
elif bmi <=27:
    result="体重超重 "
else:
    result="肥胖 "

print("您的身体质量指数为：{:.2f},属于{}".format(bmi,result))