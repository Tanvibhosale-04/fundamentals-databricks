# #approach 1 sort 
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
# def are_anagrams(s1, s2):
#     # space lowercase
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     # diff len not an anagram
#     if len(s1) != len(s2):
#         return False 
#     # Sort and compare
#     return sorted(s1) == sorted(s2)
# print(are_anagrams("LIS TE N", "silent"))  

#approch 2 count
from collections import defaultdict
def are_anagrams_count(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    count = defaultdict(int) 
    for ch in s1:
        count[ch] += 1    
    for ch in s2:
        count[ch] -= 1   
    for c in count.values():
        if c != 0:
            return False        
    return True
print(are_anagrams_count("LISten ", "silent"))
 