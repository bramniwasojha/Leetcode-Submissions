class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind=word.find(ch)
        if ind==-1:
            return word
        else:
            return word[:ind+1][::-1]+word[ind+1:]
        