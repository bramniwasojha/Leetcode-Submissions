class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total=0
        len_total=0
        for i in range(len(salary)):
            if salary[i]!=salary[0] and salary[i]!=salary[-1]:
                total+=salary[i]
                len_total+=1
        return total/len_total