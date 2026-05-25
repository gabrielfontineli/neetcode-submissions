class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = {}

        for num in nums:
            frequency_count[num] = 1 + frequency_count.get(num, 0)
        

        arr = []
        for num, cnt in frequency_count.items():
           arr.append([cnt, num])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res 
