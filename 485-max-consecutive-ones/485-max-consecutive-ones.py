class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ctr=0
        ctrmax=0
        for i in range(len(nums)):
            if nums[i]==0:
                if ctrmax<ctr:
                    ctrmax=ctr
                ctr=0
            else:
                ctr+=1
            if ctrmax<ctr:
                ctrmax=ctr
        return ctrmax
            