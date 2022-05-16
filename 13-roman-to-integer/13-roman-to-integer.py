class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=dic.get(s[-1])
        for i in range(len(s)-1):
            if dic.get(s[-2-i])>=dic.get(s[-1-i]):
                res+=dic.get(s[-2-i])
            else:
                res-=dic.get(s[-2-i])
        return res