class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for digit in digits:
            num=num*10+digit
        num+=1
        return [int(x) for x in str(num)]