class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        h={}
        for i in s:
          if i in h:
            h[i]=h.get(i,0)+1
          else:
            h[i]=1
        if len(set(h.values()))==1:
          return True
        else:
          return False