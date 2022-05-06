class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l=[first]
        for i in encoded:
            l.append(i^l[-1])
        return l