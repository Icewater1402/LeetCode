from typing import List 
class TopElements:
    '''
        Given an integer array nums and an integer k, return the k most frequent elements within the array 
        The test cases are generated that the answer is always unique 
        you may return the output in any order 
        EX: Input: nums = [1,2,2,3,3,3], k = 2 
        Output: [2,3] 
    '''
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        k_elements = {} 
        k_elements_list = []
        for i in nums:
            if(i in k_elements):
                k_elements[i] += 1
            else:
                k_elements[i] = 1
        sorted_elements = dict(sorted(k_elements.items(), key=lambda item: item[1], reverse=True))
        for position, (key, value) in enumerate (sorted_elements.items()):
            if position < k:
                k_elements_list.append(key)
            else:
                break
        return k_elements_list

    print(topKFrequent([7,7], 1))