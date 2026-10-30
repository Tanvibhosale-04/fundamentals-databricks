# If all items in your list are unique, this results in \(O(N^2)\) (quadratic) time complexity, causing severe lag on larger datasets.
#not good for production
# def most_frequent_element(lst):
#     return max(set(lst), key=lst.count)
# print(most_frequent_element([1, 2, 3, 1, 2, 1]))


# build in but slow
# from statistics import mode
# def most_frequent_mode(lst):
#     return mode(lst)
# print(most_frequent_mode([1, 2, 3, 1, 2, 1]))

# hash map
# from collections import defaultdict
# def most_frequent_dict(lst):
#     counts = defaultdict(int)
#     max_item = lst[0]
#     max_count = 0
#     for item in lst:
#         counts[item] += 1
#         if counts[item] > max_count:
#             max_count = counts[item]
#             max_item = item
#     return max_item
# print(most_frequent_dict([1, 2, 3, 1, 2, 1]))

from collections import Counter
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape']
counts = Counter(items)
top_one = counts.most_common(1) 
print(top_one)

