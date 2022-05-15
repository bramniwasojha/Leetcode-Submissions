class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        hashmap={}
        c=0
        for i in range(len(patterns)):
            if hashmap.get(patterns[i],0)!=0:
                c+=1
            else:
                if patterns[i] in word:
                    hashmap[patterns[i]]=1
                    c+=1
        return c