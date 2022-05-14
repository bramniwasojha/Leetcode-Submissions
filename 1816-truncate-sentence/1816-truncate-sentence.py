class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=s.split()
        return " ".join(l[:k])
        # c=0
        # ind=0
        # for i in range(len(s)):
        #     if s[i]==' ':
        #         c+=1
        #     if c==k:
        #         ind=i
        #         break
        # if c==k-1:
        #     ind=len(s)
        # return s[0:ind]