class Solution:
    def countSegments(self, s: str) -> int:
# APPROACH 1
        count = 0
        in_segment = False
        for char in s:
            if char != ' ':
                if not in_segment:
                    count += 1
                    in_segment = True
            else:
                in_segment = False
        return count
# APPROACH - 2
        # s1 = s.split()
        # return len(s1)
