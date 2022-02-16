class Solution:
    # couldnt be more simple
    def findMin(self, nums: list[int]) -> int:
        return min(nums)
    
    # ok lets implement a real binary search
    def findMin2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        pointer_left = 0
        pointer_right = n-1

        while pointer_left != pointer_right:
            mid = (pointer_right + pointer_left - 1) // 2
            if nums[mid] > nums[pointer_right]:
                pointer_left = mid + 1
            else:
                pointer_right = mid
        return nums[pointer_left]