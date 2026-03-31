s_list = [85, 76, 83, 79, 89]
print(s_list)

high = max(s_list)
low = min(s_list)
last_score = sum(s_list) - high - low

print("Remove highest score:",high)
print("Remove lowest score:",low)
print("Final score: {:.1f}".format(last_score))

new_list = sorted(s_list)
print("Sorted scores: \n",new_list)