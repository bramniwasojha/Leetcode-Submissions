class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split()
        l1=[""]*len(l)
        for item in l:
            index=int(item[-1])
            if index==len(l):
                l1[index-1]=item[:-1]
            else:
                l1[index-1]=item[:-1]+" "
        return "".join(l1)
