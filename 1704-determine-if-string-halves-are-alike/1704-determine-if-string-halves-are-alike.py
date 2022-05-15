class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=0
        b=0
        for i in range(len(s)):
            if i<len(s)//2:
                if s[i] in  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                    a+=1
            else:
                if s[i] in  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                    b+=1
        return a==b