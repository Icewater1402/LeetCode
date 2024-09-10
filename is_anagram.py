# NeetCode Practice
# Is Anagram? (Easy)

#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#An anagram is a string that contains the exact same characters as another string, but the order of the 
# characters can be different.

class Solution:
    def isAnagram(s: str, t: str) -> bool:
        s_hash = {} 
        t_hash = {} 

        for i in s: 
            if(i in s_hash):
                s_hash[i] += 1
            else:
                s_hash[i] = 1
        for i in t:
            if(i in t_hash):
                t_hash[i] += 1
            else:
                t_hash[i] = 1

        if(t_hash == s_hash):
            return True
        else:
            return False
    print(isAnagram("maybe", "ybeam"))