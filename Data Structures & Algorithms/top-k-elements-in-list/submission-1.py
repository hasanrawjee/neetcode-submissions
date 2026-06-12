class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countDict[n] = 1 + countDict.get(n, 0)
        for key, val in countDict.items():
            freq[val].append(key)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res