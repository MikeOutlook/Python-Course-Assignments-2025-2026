# Please complete the code according to the comments
# Do not add or delete lines of code
# Code without comment hints is complete and does not need modification

check_list = [1478, 3877, 3674, 2328, 2539,
              1613, 4088, 3991, 6461, 2691,
              1560, 3392, 3826, 4787, 2613,
              1608, 4802, 3932, 4477, 2705,
              1576, 3933, 3909, 4979, 2685]

average =sum(check_list) / len(check_list)     # Calculate average of list data, complete this line
new_list =sorted(check_list, reverse=True)    # Sort list data from largest to smallest, save to new_list

print("Average: {}".format(average))
print("Sorted from largest to smallest")
print(new_list)
