from typing import List
class Solution:
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        frequency = {}
        k_numbers = []
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        sorted_dict = {key: value for key, value in sorted(frequency.items(), key=lambda item: item[1], reverse = True)}
        #print(list(frequency.keys())[2])
        for i in range(k):
            k_numbers.append(list(sorted_dict.keys())[i])
        return k_numbers
        #print(k_numbers)
    topKFrequent([1, 2, 2, 3, 3, 3, 3], 2)