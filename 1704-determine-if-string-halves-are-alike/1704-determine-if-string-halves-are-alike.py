class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=0
        b=0
        for i in range(len(s)):
            if i<len(s)//2:
                if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                    a+=1
            else:
                if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                    b+=1
        return a==b