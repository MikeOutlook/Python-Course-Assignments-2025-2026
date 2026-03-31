import random
# Generate random float in [0,1)
print(random.random())
# Generate random integer in [1,10]
print(random.randint(1,10))
# Generate random float in [4.3, 9.1]
print(random.uniform(4.3, 9.1))
# Randomly select one element from list list1
list1 = [11,26,35,42,50]
print(random.choice(list1))