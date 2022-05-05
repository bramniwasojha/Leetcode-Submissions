class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in sentences:
            s=i.split(' ')
            if len(s)>m:
                m=len(s)
        return m