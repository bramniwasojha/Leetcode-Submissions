class Solution:
    def checkString(self, s: str) -> bool:
        a=0
        for e in s:
            if e=='b':
                a=1
            if e=='a' and a==1:
                return False
        return True
                