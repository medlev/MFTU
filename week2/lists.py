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
"""

#program exaple
import this
zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
"""
import operator
zen_map = dict()
for word in zen.split():
    cleaned_word = word.strip('.,!-').lower()
    if cleaned_word not in zen_map:
        zen_map[cleaned_word] = 0
    zen_map[cleaned_word] += 1
#print(zen_map)

zen_items = zen_map.items()
word_count_items = sorted (
    zen_items, key = operator.itemgetter(1), reverse = True
)
print(word_count_items[:3])

"""
from collections import Counter
cleaned_list = []
for word in zen.split():
    cleaned_list.append(word.strip(',.-!').lower())
print(Counter(cleaned_list).most_common(3))