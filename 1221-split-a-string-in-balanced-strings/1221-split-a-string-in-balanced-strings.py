class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        status=0
        for i in range(0,len(s)):
            if s[i]=='L':
                status+=1
                if status==0:
                    c+=1
            elif s[i]=='R':
                status-=1
                if status==0:
                    c+=1
        return c