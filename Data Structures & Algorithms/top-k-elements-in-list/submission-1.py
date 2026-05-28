class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: list of numbers
        # Amount of repetitions per number -> HashMap
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Reverse the key and value in the map
        arr = []

        for num, cnt in count.items():
            arr.append([cnt, num]);

        # Sort the items by the value
        arr.sort()

        # Flip back and print the highest value numbers
        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        # Output: the k most repeated numbers
        return res
