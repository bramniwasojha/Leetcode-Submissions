class Solution:
    def maximum69Number (self, num: int) -> int:
        snum=str(num)
        for i in range(len(snum)):
            if snum[i] == '6':
                return int(snum[:i]+'9'+snum[i+1:])
        return num