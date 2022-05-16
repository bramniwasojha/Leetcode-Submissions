class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low==high and low%2==0:
            return 0
        if low==high and low%2!=0:
            return 1
        if high-low==1:
            return 1
        if low%2==0 and high%2==0:
            return (high-low)//2
        if low%2==0 and high%2!=0:
            return 1+((high-low)//2)
        if low%2!=0 and high%2==0:
            return 1+((high-low)//2)
        if low%2!=0 and high%2!=0:
            return 1+((high-low)//2)
        return 