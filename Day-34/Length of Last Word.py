class Solution:
    def lengthOfLastWord(self, s: str) -> int:
# 1st Approach
        length = 0
        i = len(s)-1
        while i>=0 and s[i] == " ":
            i=i-1
        while i>=0 and s[i] != " ":
            length+=1
            i-=1
        return length
# 2nd Approach 
        # splitted_words = s.split()
        # return (len(splitted_words[-1]))

        
