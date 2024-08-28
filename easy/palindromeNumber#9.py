#Code by Kashyap Sukshavasi

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xStr = str(x)
        arr = []
        for i in xStr:
            arr.append(i)
        if arr == arr[::-1]:
            return True
        return False
    
#Time Complexity: O(n)
#Space Complexity: O(n)