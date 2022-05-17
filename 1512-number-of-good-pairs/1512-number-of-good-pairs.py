class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=0
        for num in set(nums):
            n=nums.count(num)
            res+=(n*(n-1))//2
        return res