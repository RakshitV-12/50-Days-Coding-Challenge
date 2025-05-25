class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(left=True):
            low, high = 0, len(nums) - 1
            res = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    res = mid
                    if left:
                        high = mid - 1  # Move left
                    else:
                        low = mid + 1  # Move right
            
            return res
        
        start = binary_search(left=True)
        end = binary_search(left=False)
        
        return [start, end]
