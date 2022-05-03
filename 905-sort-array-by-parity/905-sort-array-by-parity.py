class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        for num in nums:
            if num%2==0:
                l.append(num)
        for num in nums:
            if num%2!=0:
                l.append(num)
        return l