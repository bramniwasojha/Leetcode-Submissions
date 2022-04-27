class Solution:
    def checkString(self, s: str) -> bool:
        flag=0
        for letter in s:
            if letter=='b':
                flag=1
            if letter=='a' and flag==1:
                    return False
        return True
                