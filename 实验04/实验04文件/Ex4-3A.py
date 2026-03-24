s_list = [85, 76, 83, 79, 89]
print(s_list)

high = max(s_list)
low = min(s_list)
last_score = sum(s_list) - high - low

print("去掉最高分",high)
print("去掉最低分",low)
print("最终得分是{:.1f}".format(last_score))

new_list = sorted(s_list)
print("排序后的分数是： \n",new_list)