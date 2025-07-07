class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0  # non-zero elements kahan rakhne hain

        # Step 1: Move all non-zero elements to front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZero] = nums[i]
                lastNonZero += 1

        # Step 2: Fill remaining with 0s
        for i in range(lastNonZero, len(nums)):
            nums[i] = 0