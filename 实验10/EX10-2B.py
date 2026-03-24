import matplotlib.pyplot as plt
#中文字体显示修正，在下面填写正确的代码
plt.rcParams["font.family"] = ["SimHei"]

data = [32, 187, 42, 29, 44, 38]
pieLabel = ["外伤和中毒", "恶性肿瘤", "脑血管疾病", "内分泌疾病", "心血管疾病", "呼吸系统疾病"]
pieColor =["r","g","pink","y","m","b"] #产生颜色数据列表，将本行代码补充完整
pieExplode =[0,0,0.1,0,0,0.2] #产生突出值数据列表，将本行代码补充完整

plt.pie(data,labels=pieLabel,colors=pieColor,explode=pieExplode,
        autopct="%.1f%%",shadow=True) #调用函数绘制饼图，将本行代码补充完整

plt.show()

