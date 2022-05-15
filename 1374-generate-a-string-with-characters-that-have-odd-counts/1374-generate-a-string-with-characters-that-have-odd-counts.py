class Solution:
    def generateTheString(self, n: int) -> str:
        res='a'
        if n%2==0:
            res+='b'*(n-1)
        else:
            res+='a'*(n-1)
        return res