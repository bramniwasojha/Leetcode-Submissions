class Solution:
  def digitCount(self, num: str) -> bool:
    c=0
    for i in range(len(num)):
      if num.count(str(i))==int(num[i]):
        c+=1
    if c==len(num):
      return True
    else:
      return False