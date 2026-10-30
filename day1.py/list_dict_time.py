import timeit

my_list = [10, 20, 30, 40, 50]
my_dict = {10: "A", 20: "B", 30: "C", 40: "D", 50: "E"}

# 1. Search
print("LIST SEARCH:")
print(timeit.timeit(lambda: my_list.index(50), number=10000))

print("DICT LOOKUP:")
print(timeit.timeit(lambda: my_dict[50], number=10000))

# 2. Membership check
print("LIST MEMBERSHIP:")
print(timeit.timeit(lambda: 50 in my_list, number=10000))

print("DICT MEMBERSHIP:")
print(timeit.timeit(lambda: 50 in my_dict, number=10000))