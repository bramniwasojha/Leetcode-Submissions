from math import log 
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res=1
        while True:
            if res==n:
                return True
            if res>n:
                return False
            res*=2
    