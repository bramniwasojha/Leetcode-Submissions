class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ['a','c','e','g']:
          if coordinates[1] in ['1','3','5','7']:
            return False
          else:
            return True
        else:
          if coordinates[1] in ['1','3','5','7']:
            return True
          else:
            return False