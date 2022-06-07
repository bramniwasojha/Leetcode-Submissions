class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        for str in strs:
            while first and not str.startswith(first):
                first=first[:-1]
        return first

        
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         l=min([len(str) for str in strs])  
#         c=""
#         for i in range(l):
#             s=[str[i] for str in strs]
#             if len(set(s))==1:
#                 c+=s[0]
#             else:
#                 break
#         return c