def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for i, char in enumerate(s):
            last_seen[char] = i  
            if all(last_seen.values()) or min(last_seen.values()) >= 0:
                count += min(last_seen.values()) + 1 
        return count


