class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create hash
        seen = set()

        # Iterate through array
        for num in nums:
            if num in seen:
                return True
            # Add to Array
            seen.add(num)
        return False



        