#Code by Kashyap Sukshavasi
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #empty dictionary
        dictionary = {}

        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    

        for key in dictionary:
            if dictionary[key] > len(nums)/2:
                return key