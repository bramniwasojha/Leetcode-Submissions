from collections import deque
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res=deque()
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res