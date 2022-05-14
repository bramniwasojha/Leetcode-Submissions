class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        hashmap={}
        for i in range(len(words)):
            temp=0
            for j in range(len(words[i])):
                if hashmap.get(words[i][j],0)!=0:
                    continue
                else:
                    if words[i][j] in allowed:
                        hashmap[words[i][j]]=1
                    else:
                        temp=1
                        break
            if temp==0:
                c+=1
                        
        return c