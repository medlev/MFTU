#w2e1
"""
empty_list = [ ]
empty_list = list()

none_list = [None] * 10
collections = ["list", "tuple", "dict", "set"]

user_data = [
    ["Elena", 4.4],
    ["Andrew", 4.2]
]
print(user_data)

for idx, collection in enumerate(collections):
    print("#{} {}".format(idx, collection)) 
"""

#w2e2
import random
numbers = []
numbers_size = random.randint(10, 15)
for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))
print(numbers)

numbers.sort()
print(numbers)

half_size = len(numbers) // 2
median = None

if numbers_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2
print(median)