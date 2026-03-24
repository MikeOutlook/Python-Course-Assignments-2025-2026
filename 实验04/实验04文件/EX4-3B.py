#请按注释要求完成代码
#不能增加、删除代码行
#没有注释提示的代码为完整代码不需要修改

check_list = [1478, 3877, 3674, 2328, 2539,
              1613, 4088, 3991, 6461, 2691,
              1560, 3392, 3826, 4787, 2613,
              1608, 4802, 3932, 4477, 2705,
              1576, 3933, 3909, 4979, 2685]

average =sum(check_list) / len(check_list)     # 求列表数据的平均值，将本行代码补充完整
new_list =sorted(check_list, reverse=True)    # 将列表数据从大到小排序，结果保存到新列表new_list

print("平均值是{}".format(average))
print("从大到小排序")
print(new_list)
