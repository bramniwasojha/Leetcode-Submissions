class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_=max(candies)
        for i in range(len(candies)):
            if (candies[i]+extraCandies)>=max_:
                candies[i]=True
            else:
                candies[i]=False
        return candies
        # l=[]
        # max_=max(candies)
        # for i in candies:
        #     if (i+extraCandies)>=max_:
        #         l.append(True)
        #     else:
        #         l.append(False)
        # return l