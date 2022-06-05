class Solution:
    def squareIsWhite(self, c: str) -> bool:
        if c[0] == 'a' or c[0] =='c' or c[0] =='e' or c[0] =='g':
          if c[1] =='1' or c[1] =='3' or c[1] =='5' or c[1] =='7':
            return False
          else:
            return True
        else:
          if c[1] =='1' or c[1] =='3' or c[1] =='5' or c[1] =='7':
            return True
          else:
            return False