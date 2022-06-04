#using memoization
class Solution:
    def fib(self, n: int) -> int:
        l=[0,1]
        for i in range(2,n+1):
            l.append(l[i-1]+l[i-2])
        return l[n]
    
#recursive   
# class Solution:
#     def fib(self, n: int) -> int:
#         if n<2:
#             return n
#         return self.fib(n-1)+self.fib(n-2)