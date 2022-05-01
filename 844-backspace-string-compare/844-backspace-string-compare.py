class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        s1=""
        for l in s:
            if l=='#':
                if stack: 
                    stack.pop()
            else:
                stack.append(l)
        s1="".join(stack)
        stack=[]
        for l in t:
            if l=='#':
                if stack: 
                    stack.pop()
            else:
                stack.append(l)
        t1="".join(stack)
        if s1==t1:
            return True
        else:
            return False

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s1=""
        # s2=""
        # for i in range(len(s)):
        #     if i=='#':
        #         s1=s.replace(s[i-1:i+1],"")
        # for i in range(len(t)):
        #     if i=='#':
        #         t=t.replace(t[i-1:i+1],"")
        # if s==t:
        #     return True
        # else:
        #     return False