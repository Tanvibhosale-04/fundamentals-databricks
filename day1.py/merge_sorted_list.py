# def merge_sorted_lists(list1, list2):#using sorted with concatenation 
#   return sorted(list1 + list2)
# print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))


# #heapq.merge(a, b) merges two sorted lists without creating extra copies.
# It returns an iterator, so we convert it into a list.
# This method is memory-efficient and works well for large datasets.
#  import heapq 
# a = [1, 3, 5]
# b = [2, 4, 6]
# c = list(heapq.merge(a, b))
# print(c)

# chain(a, b) merges lists without creating intermediate copies.
# sorted() ensures the result remains ordered.
# This is a simple one-liner but involves extra sorting.
from itertools import chain
a = [1, 3, 5]
b = [2, 4, 6]
c = list(sorted(chain(a, b)))
print(c)
