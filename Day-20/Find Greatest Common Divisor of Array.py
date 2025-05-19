def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        return gcd(smallest, largest)
def gcd(a, b):
      while b:
          a, b = b, a % b
      return a
