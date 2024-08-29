#Code by Kashyap Sukshavasi

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        #Convert binary string to integer, step #1
        a_int = int(a, 2)
        b_int = int(b, 2)

        sum = a_int + b_int

        return bin(sum)[2:]
