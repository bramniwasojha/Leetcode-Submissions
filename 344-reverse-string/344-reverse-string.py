class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        # for i in range(len(s)//2):
        #     temp=s[i]
        #     s[i]=s[len(s)-1-i]
        #     s[len(s)-1-i]=temp