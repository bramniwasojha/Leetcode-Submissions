class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        s=""
        i=0
        while i<l1 or i<l2:
            if len(s)==(2*l1):
                s+=word2[i:]
                break
            elif len(s)==(2*l2):
                s+=word1[i:]
                break
            else:
                s+=word1[i]
                s+=word2[i]
            i+=1
        return s