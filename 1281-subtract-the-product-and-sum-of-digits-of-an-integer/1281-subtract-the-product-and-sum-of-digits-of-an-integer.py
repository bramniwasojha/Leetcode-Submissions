class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        add=0
        l=[]
        while n>0:
            l.append(n%10)
            n=n//10
            
        for n in l:
            pro=pro*n
            add=add+n
            
        return pro-add
