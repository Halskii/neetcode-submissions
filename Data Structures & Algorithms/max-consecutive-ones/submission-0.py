class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_number = 0
        for number in nums:
            if number == 1:
                count += 1
                max_number = max(count, max_number)
            else:
                count = 0
        return max_number