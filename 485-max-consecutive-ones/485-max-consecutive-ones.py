class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ctr=0
        maxctr=0
        for num in nums:
            if num==1:
                ctr+=1
            else:
                if ctr>maxctr:
                    maxctr=ctr
                ctr=0
        
        if maxctr>ctr:
            return maxctr
        else:
            return ctr