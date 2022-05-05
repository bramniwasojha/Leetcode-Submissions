from collections import deque
class Solution:
    def minimumSum(self, num: int) -> int:
        l=list(str(num))
        sl=sorted(l)
        return int(sl[0]+sl[-1])+int(sl[1]+sl[2])