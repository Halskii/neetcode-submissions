class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #Okay so we have two indices and we need to find out at which indices would the value add up to the target, to do so we can brute force it or we can do it the smarter way and take the difference, and search a map for the difference.
        numMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if (diff in numMap):
                return [numMap[diff], i]
            numMap[n] = i
            
