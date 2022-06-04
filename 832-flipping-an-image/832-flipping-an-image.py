class Solution:
  def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    for row in image:
      for i in range(len(row)//2):
        row[i],row[len(row)-1-i]=row[len(row)-1-i],row[i]
      for i in range(len(row)):
        if row[i]==0:
          row[i]=1
        else:
          row[i]=0
    return image