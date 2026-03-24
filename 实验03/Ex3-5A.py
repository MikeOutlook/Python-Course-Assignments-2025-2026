genderList = ["女士","先生"] # 创建性别列表
IDcard = input("请输入身份证号码")
gender = int(IDcard[-2]) # 取出倒数第二位
genderID = gender % 2 # 获取余数
greet = genderList[genderID] # 通过余数从性别列表索引数据
print(greet,"你好")