class Solution:
    def freqAlphabets(self, s: str) -> str:
        s1=""
        revs=s[::-1]
        i=0
        while i<len(revs):
            if revs[i]=="#":
                s1+=chr(96+int(revs[i+1:i+3][::-1]))
                i+=3
            else:
                s1+=chr(96+int(revs[i]))
                i+=1
        return s1[::-1]