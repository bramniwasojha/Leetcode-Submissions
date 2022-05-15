class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f=''
        s=''
        t=''
        for l in firstWord:
            f+=str(ord(l)-97)
        for l in secondWord:
            s+=str(ord(l)-97)
        for l in targetWord:
            t+=str(ord(l)-97)
        if int(f)+int(s)==int(t):
            return True
        return False