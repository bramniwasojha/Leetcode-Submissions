class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=0
        b=0
        i=0
        j=len(s)-1
        v={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while i<=j:
            if s[i] in v:
                a+=1
            if s[j] in v:
                b+=1
            i+=1
            j-=1
        return a==b