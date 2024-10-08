#Code by Kashyap Sukshavasi

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(0, len(nums)):
            num = nums[i]
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
    
#Time Complexity: O(n)
#Space Complexity: O(n)