class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[]
        for w in words:
            s=""
            for c in w:
                s+=l[ord(c)-ord('a')]
            res.append(s)
        return len(set(res))