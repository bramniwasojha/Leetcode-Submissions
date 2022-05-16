class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s=s[::-1]
        res=dic[s[0]]
        for i in range(len(s)-1):
            if dic[s[i]]<=dic[s[i+1]]:
                res+=dic[s[i+1]]
            else:
                res-=dic[s[i+1]]
        return res