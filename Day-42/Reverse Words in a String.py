class Solution:
    def reverseWords(self, s: str) -> str:
    # 1st Approach 
        # return " ".join(s.split()[::-1])
    # 2nd Approach 
        words = []
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i >= n:
                break
            start = i
            while i < n and s[i] != " ":
                i += 1
            words.append(s[start:i])
        return " ".join(words[::-1])


