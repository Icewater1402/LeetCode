# NeetCode Practice
# Anagram Groups (Medium)
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#An anagram is a string that contains the exact same characters as another string, but the order of the 
# characters can be different.
# GPT Insight: two hash maps can be compared if they have the same keys and values. Order does not matter 
from typing import List
class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        # solution: sorted string is your key and a list of strings will be your value 
        list_dict = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word in list_dict:
                list_dict[sorted_word].append(i)
            else:
                list_dict[sorted_word] = [i]
        return list(list_dict.values())

    print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))