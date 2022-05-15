class Solution:
    def replaceDigits(self, s: str) -> str:
        s1=""
        for i in range(len(s)):
            if s[i].isalpha():
                    s1+=s[i]
            else:
                s1+=chr(ord(s[i-1])+int(s[i]))
        return s1