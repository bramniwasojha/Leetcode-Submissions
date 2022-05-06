class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        add=0
        while n>0:
            rem=n%10
            pro*=rem
            add+=rem
            n//=10
        return pro-add
