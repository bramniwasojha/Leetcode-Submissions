class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        
        # nums1=nums.sort()
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    c+=1
            res.append(c)
        return res