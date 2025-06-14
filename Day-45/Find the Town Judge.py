class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # APPROACH
        trust_score = [0] * (n + 1)  # Using 1-based indexing
        for a, b in trust:
            trust_score[a] -= 1  # a trusts someone -> less likely to be judge
            trust_score[b] += 1  # b is trusted -> more likely to be judge

        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i  # this person is trusted by everyone else and trusts no one

        return -1  # no judge found
