class Solution:
    def sortSentence(self, s: str) -> str:
        s1=[item[-1]+item[:-1] for item in s.split()]
        s1.sort()
        l=[item[1:] for item in s1]
        return " ".join(l)