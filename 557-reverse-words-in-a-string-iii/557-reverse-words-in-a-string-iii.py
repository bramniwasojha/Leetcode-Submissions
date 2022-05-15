class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        return " ".join([item[::-1] for item in l])