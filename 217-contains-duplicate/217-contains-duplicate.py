class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            if hashmap.get(nums[i],0)!=0:
                return True
            hashmap[nums[i]]=1
        return False