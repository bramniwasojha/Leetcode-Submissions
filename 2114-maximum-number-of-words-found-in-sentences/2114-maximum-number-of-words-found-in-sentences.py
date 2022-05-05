class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=0
        for i in sentences:
            maxlen=i.count(" ")+1
            if res<maxlen:
                res=maxlen
        return res