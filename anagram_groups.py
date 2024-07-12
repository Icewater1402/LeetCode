# NeetCode Practice
# Anagram Groups (Medium)

from typing import List
class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagrams = []
        if len(strs) == 1:
            anagrams.append(strs)
            return anagrams
        anagram_hash = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if(sorted_word in anagram_hash):
                anagram_hash[sorted_word].append(i)
            else:
                anagram_hash[sorted_word] = [i]
        return list(anagram_hash.values())
    

            
    strings = ["act", "pots", "tops", "cat", "stop", "hat"]
    answer = groupAnagrams(strings)
    print(answer)