class Solution:
  def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    image=[row[::-1] for row in image]
    for row in image:
      for i in range(len(row)):
        if row[i]==0:
          row[i]=1
        else:
          row[i]=0
    return image