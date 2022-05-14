class Solution:
    def countPoints(self, rings: str) -> int:
        c=0
        for i in range(0,10):
            if 'B'+str(i) in rings and 'G'+str(i) in rings and 'R'+str(i) in rings:
                c+=1
        return c