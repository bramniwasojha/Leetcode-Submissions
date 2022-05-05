class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for ele in operations:
            if ele[0]=='-' or ele[-1]=='-':
                x-=1
            else:
                x+=1
        return x