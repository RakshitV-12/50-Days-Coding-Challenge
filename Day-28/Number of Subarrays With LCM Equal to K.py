class Solution:
    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x
    def lcm(self, x, y):
        return (x * y) // self.gcd(x, y)

    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            current_lcm = nums[i]
            if current_lcm == k:
                count += 1

            for j in range(i + 1, n):
                current_lcm = self.lcm(current_lcm, nums[j])
                if current_lcm > k:
                    break
                if current_lcm == k:
                    count += 1
        
        return count
