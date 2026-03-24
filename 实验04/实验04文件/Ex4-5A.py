import random
# 随机产生[0,1) 之间的小数
print(random.random())
# 随机产生[1,10] 间的整数
print(random.randint(1,10))
# 随机产生[4.3, 9.1] 之间的小数
print(random.uniform(4.3, 9.1))
# 从列表 list1 中随机抽取一个元素
list1 = [11,26,35,42,50]
print(random.choice(list1))