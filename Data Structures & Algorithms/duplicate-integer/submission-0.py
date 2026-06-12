class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()

        for n in nums:
            if n in uniqueSet:
                return True
            uniqueSet.add(n)
        
        return False