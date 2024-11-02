from typing import List
# Given an integer array 'nums' return an array 'output' where 'output[i] is the product of all the elements of nums except nums[i] 
# each product is guaranteed to fit in a 32-bit integer
#ex: input: nums = [1,2,4,6]
#    output: [48,24,12,8]
class ProductsOfArray:
    def productExceptSelf(nums: List[int]) -> List[int]:
        mult_array = []
        for index in range(len(nums)):
            product = 1
            for sec_index in range(len(nums)):
                if(sec_index == index):
                    pass 
                else:
                    product *= nums[sec_index] 
            mult_array.append(product)
        return mult_array
    print(productExceptSelf([1,2,4,6]))

# this could probably be optimized to O(n) since the problem challenges us to do so
# im sure we could use a placeholder or something to make it so that we dont have to iterate through the loop twice 
    