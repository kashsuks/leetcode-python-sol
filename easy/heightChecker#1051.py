#imports
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #Sort the array
        expected = sorted(heights)

        #counter
        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count