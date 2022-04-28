class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum=0
        for item in accounts:
            if sum(item)>maxsum:
                maxsum=sum(item)
        return maxsum