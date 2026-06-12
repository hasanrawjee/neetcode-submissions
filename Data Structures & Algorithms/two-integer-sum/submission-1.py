class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numList = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in numList:
                return [numList[diff], i]
            
            numList[n] = i