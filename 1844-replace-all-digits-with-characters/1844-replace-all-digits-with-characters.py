class Solution:
    def replaceDigits(self, s: str) -> str:
        s1=""
        for i in range(0,len(s)-1,2):
            s1+=s[i]+str(chr(ord(s[i])+int(s[i+1])))
        if s[-1].isalpha():
            s1+=s[-1]
        return s1