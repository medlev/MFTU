#example 1
"""
empty_set = set()
number_set = {1, 2, 3, 3, 4, 5}
print(number_set)
print(2 in number_set)
"""

#example 2
"""
odd_set = set()
even_set = set()
for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)
print(odd_set)
print(even_set)
"""

#example 3
odd_set = set()
even_set = set()
for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)
union_set = odd_set | even_set
union_set = odd_set.union(even_set)
print(union_set)

intersect_set = odd_set & even_set
intersect_set = odd_set.intersection(even_set)
print(intersect_set)

difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)
print(difference_set)

symmetric_difference_set = odd_set ^ even_set
symmetric_difference_set = odd_set.symmetric_difference(even_set)
print(symmetric_difference_set)

#example 4
even_set.remove(2)
print(even_set)