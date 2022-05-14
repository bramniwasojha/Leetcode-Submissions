class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for w in words:
            for c in w:
                if c not in allowed:
                    count -= 1
                    break
        return count