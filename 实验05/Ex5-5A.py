temp_list = [37.7, 37.5, 37.3, 36.8, 38.4, 37.4,
             37.7, 36.3, 39.0, 38.5, 37.8, 37.3,
             36.6, 36.2, 37.5, 37.6, 38.6, 36.9,
             38.2, 37.9]
heat_list = []
for temp in temp_list:
    if temp > 37.3:
        f = temp * 1.8 + 32
        f1 = round(f, 1)
        heat_list.append(f1)
print(heat_list)