class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                if res<len(stack):
                    res=len(stack)
                stack.pop()
        return res
                