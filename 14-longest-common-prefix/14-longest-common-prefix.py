class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=min([len(str) for str in strs])  
        c=""
        for i in range(l):
            s=[str[i] for str in strs]
            if len(set(s))==1:
                c+=s[0]
            else:
                break
        return c