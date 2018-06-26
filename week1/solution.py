import sys

digit_string = sys.argv[1]
digit_sum = sum(map(int, digit_string))
print(digit_sum)