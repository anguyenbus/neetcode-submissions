class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) //2
            if nums[mid] > nums[right]:
                # mid is in the left (bigger) part, so the drop is after mid
                left = mid + 1
            else:
                # mid is in the right (smaller) part, so mid may be the answer
                right = mid
        return nums[left]