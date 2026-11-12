class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenIt = set()
        for n in nums:
            if n in seenIt:
                return True
            seenIt.add(n)
    
        return False